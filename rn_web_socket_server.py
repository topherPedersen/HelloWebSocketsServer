#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def web_socket_server(websocket, path):

	message_from_client = await websocket.recv()

	print("Message From Client: " + str(message_from_client))

    server_response = "hello, websockets"

	await websocket.send(server_response)

start_server = websockets.serve(web_socket_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()