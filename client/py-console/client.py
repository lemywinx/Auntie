#!/usr/bin/env python3

import asyncio
from getch import _Getch 

getchar = _Getch()

async def character_grab():
    while True:
        c = getchar()
        print (c)
        if c == '\x03':
            break
        reply = await tcp_echo_client(c)

async def tcp_echo_client(message: str):
    reader, writer = await asyncio.open_connection(
        '192.168.7.113', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    writer.close()
    await writer.wait_closed()

#asyncio.run(tcp_echo_client(character_grab()))
asyncio.run(character_grab())

