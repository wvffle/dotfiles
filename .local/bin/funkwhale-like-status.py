#!/bin/python

# NOTE: Check out the client: https://github.com/wvffle/userscripts/blob/main/funkwhale/like-button-in-waybar.user.js

import aiohttp.web
import asyncio
import socket
import sys
import os


HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', 9912))

clients = []
sockets = []


async def http_handler(request):
    res = aiohttp.web.Response(text="", content_type="text/html")

    for ws in sockets:
        await ws.send_str('1')

    return res


async def _write(string):
    sys.stdout.write(f"{string}\n")
    sys.stdout.flush()

    for ws in clients:
        await ws.send_str(string)


async def websocket_handler(request):
    ws = aiohttp.web.WebSocketResponse()
    ws.headers['Access-Control-Allow-Origin'] = '*'
    await ws.prepare(request)
    sockets.append(ws)
    last_state = None

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            state = msg.data

            if state != last_state:
                last_state = state

                if state == "1":
                    await _write("󰋑")

                if state == "0":
                    await _write("󰋕")

    sockets.remove(ws)
    return ws


async def ws_client_handler(request):
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)
    clients.append(ws)

    async for msg in ws:
        pass

    clients.remove(ws)
    return ws

# waybar executes program per output, 
# hence we need to connect to the websocket and get the state asynchronously
async def ws_client():
    session = aiohttp.ClientSession()
    async with session.ws_connect(f'http://{HOST}:{PORT}/client') as ws:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                await _write(msg.data)
    await session.close()


if __name__ == '__main__':
    # If it's a second opened program, listen to the websocket for changes
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if s.connect_ex((HOST, PORT)) == 0:
            asyncio.run(ws_client())
            exit()

    app = aiohttp.web.Application()
    app.router.add_route('GET', '/', websocket_handler)
    app.router.add_route('GET', '/client', ws_client_handler)
    app.router.add_route('POST', '/', http_handler)
    aiohttp.web.run_app(app, host=HOST, port=PORT)
