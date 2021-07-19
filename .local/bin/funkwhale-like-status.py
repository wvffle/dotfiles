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

routes = aiohttp.web.RouteTableDef()

async def _handler(request, msg):
    res = aiohttp.web.Response(text="", content_type="text/html")

    for ws in sockets:
        await ws.send_str(msg)

    return res


async def _write(string):
    sys.stdout.write(f"{string}\n")
    sys.stdout.flush()

    for ws in clients:
        await ws.send_str(string)


@routes.post('/')
async def toggle_like(request):
    return await _handler(request, '1')


@routes.post('/like')
async def like(request):
    return await _handler(request, '2')


@routes.post('/dislike')
async def dislike(request):
    return await _handler(request, '3')


@routes.get('/')
async def ws_server(request):
    ws = aiohttp.web.WebSocketResponse()
    ws.headers['Access-Control-Allow-Origin'] = '*'
    await ws.prepare(request)

    sockets.append(ws)
    last_state = None

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT and msg.data != last_state:
            last_state = msg.data
            await _write("󰋑" if last_state == '1' else "󰋕")

    sockets.remove(ws)
    return ws


@routes.get('/client')
async def ws_client(request):
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)
    clients.append(ws)

    async for msg in ws:
        pass

    clients.remove(ws)
    return ws


async def main():
    session = aiohttp.ClientSession()
    async with session.ws_connect(f'http://{HOST}:{PORT}/client') as ws:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                await _write(msg.data)

    await session.close()


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if s.connect_ex((HOST, PORT)) == 0:
            asyncio.run(main())
            exit()

    app = aiohttp.web.Application()
    app.add_routes(routes)
    aiohttp.web.run_app(app, host=HOST, port=PORT)
