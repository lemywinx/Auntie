#!/usr/bin/env python3

import asyncio
from getch import _Getch
import sys
import json

getchar = _Getch()

if len(sys.argv) < 1:
    print("Usage: client.py <addr>")
    sys.exit(1)
server_addr = sys.argv[1]

MOVE_MAPPING = {
    'w': [0, -1],
    'a': [-1, 0],
    's': [0, 1],
    'd': [1, 0],
}

def user_message(s: str):
    print(s)

async def main_client_loop():
    while True:
        c = getchar()
        cmd = None

        if c == '\x03':
            break

        if c in MOVE_MAPPING:
            cmd = {"move": MOVE_MAPPING[c]}

        if cmd != None:
            jsoncmd = json.dumps({"command": cmd})
            reply = await tcp_echo_client(jsoncmd)

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(server_addr, 26969)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    writer.close()
    await writer.wait_closed()

#asyncio.run(tcp_echo_client(main_client_loop()))
asyncio.run(main_client_loop())

