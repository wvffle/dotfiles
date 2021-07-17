#!/bin/python

# NOTE: Check out the client: https://github.com/wvffle/userscripts/blob/main/funkwhale/like-button-in-waybar.user.js

from xdg.BaseDirectory import save_cache_path
import aiohttp.web
import asyncio
import signal
import atexit
import sys
import os


HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', 9912))

sockets = []
pidfile = save_cache_path('funkwhale-like') + '/pid'
fifo = save_cache_path('funkwhale-like') + '/fifo'


def signal_handler(sig, frame):
    exit()


def exit_handler():
    with open(pidfile, 'r') as file:
        os.system(f'kill -9 {file.read()}')
    os.remove(pidfile)


async def http_handler(request):
    res = aiohttp.web.Response(text="", content_type="text/html")

    for ws in sockets:
        await ws.send_str('1')

    return res


async def websocket_handler(request):
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)
    sockets.append(ws)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            with open(fifo, 'w') as file:
                file.write(msg.data)

    sockets.remove(ws)
    return ws


def print_fifo():
    last_state = None

    while True:
        state = None
        with open(fifo, 'rb', 0) as file:
            state = file.read(1).decode()

        if state != last_state:
            last_state = state

            if state == "1":
                sys.stdout.write("󰋑\n")
                sys.stdout.flush()

            if state == "0":
                sys.stdout.write("󰋕\n")
                sys.stdout.flush()


if __name__ == '__main__':
    if not os.path.exists(fifo):
        os.mkfifo(fifo)

    if os.path.exists(pidfile):
        print_fifo()
        exit()

    with open(pidfile, 'w') as file:
        pass

    atexit.register(exit_handler)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    pid = os.fork()

    if pid == 0:
        app = aiohttp.web.Application()
        app.router.add_route('GET', '/', websocket_handler)
        app.router.add_route('POST', '/', http_handler)
        aiohttp.web.run_app(app, host=HOST, port=PORT)
        exit()

    with open(pidfile, 'w') as file:
        file.write(f'{pid}')
    
    print_fifo()
