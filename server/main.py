#!/usr/bin/env python3

import asyncio
import json
from pprint import pprint

GAME_BOARD = [
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_','_','_'],
]

player_position = [0, 0]

async def handle_echo(reader, writer):
    try:
        data = await reader.read(100)
        message = data.decode()
        parsed = json.loads(message)

        #addr = writer.get_extra_info('peername')
        #print(parsed)

        x = parsed["command"]["move"]
        GAME_BOARD[player_position[1]][player_position[0]] = '_'
        player_position[0] += x[0]
        player_position[1] += x[1]
        GAME_BOARD[player_position[1]][player_position[0]] = '@'

        print("\n".join(["".join(row) for row in GAME_BOARD]))

        #writer.write(data)
        #await writer.drain()

        writer.close()
    except:
        pass

async def main():
    server = await asyncio.start_server(handle_echo, '0.0.0.0', 26969)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
