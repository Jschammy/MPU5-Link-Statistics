"""
Copyright (c) 2025, Persistent Systems LLC

Permission to use, copy, modify, and/or distribute this software
for any purpose with or without fee is hereby granted,
provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS
ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING
ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL,
DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE
OR PERFORMANCE OF THIS SOFTWARE.
"""

import websockets
from websockets.protocol import State
import ssl
import asyncio
import json


class WRApiClient:
    def __init__(self,query_ip):
        self.ip=query_ip
        self.loop = asyncio.get_event_loop()
        self.uri = "wss://"+self.ip
        self.ssl_context = self.__set_ssl_context__()
        self.connection = self.__start_connection__()
        self.sleep_timer = 0.5

    def __set_ssl_context__(self):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        return ssl_context

    @staticmethod
    def __connection_is_open(connection):
        """Backwards compatibility with websockets version 13.1"""
        if connection is None:
            return False

        # check for version 13.1 (WebSocketClientProtocol)
        if getattr(connection, 'open', False):
            return True

        # check for version 14.1 (ClientConnection)
        if getattr(connection, 'state', None) == State.OPEN:
            return True

        return False

    def __start_connection__(self):
        return self.loop.run_until_complete(self.__connect__())

    async def __connect__(self):
        connection = await websockets.connect(uri=self.uri, ssl=self.ssl_context)
        if self.__connection_is_open(connection):
            return connection
        else:
            print("Connection not established")
            return None

    def send(self, message):
        """Send a JSON API message to the client"""
        message = json.dumps(message)
        self.loop.run_until_complete(self.__send_message__(message))

    async def __send_message__(self, message):
        await self.connection.send(message)
        await asyncio.sleep(self.sleep_timer)

    def receive(self):
        """Receive the JSON API response from the server"""
        new_msg = self.loop.run_until_complete(self.__recv_message__())
        return json.loads(new_msg)

    async def __recv_message__(self):
        return await self.connection.recv()

    def set_sleep_timer(self, seconds):
        """Set the time to sleep after sending an API message."""
        self.sleep_timer = seconds