import websockets
from websockets.legacy.server import WebSocketServerProtocol
import asyncio
import json
from wsminepy import event
from wsminepy import command


class Server:
    def __init__(self) -> None:
        self.__init = None
        self.__listener = {}
        self.websocket: WebSocketServerProtocol

    async def parse_message(self, message: dict):
        messagePurpose = message['header']['messagePurpose']
        if messagePurpose == 'event':
            eventname = message["header"]["eventName"]
            if eventname in self.__listener:
                if callable(self.__listener[eventname]):
                    await self.__listener[eventname](message["body"])
            if "all" in self.__listener:
                if callable(self.__listener["all"]):
                    await self.__listener["all"](eventname, message["body"])

    async def receive(self, websocket: WebSocketServerProtocol, _: str):
        self.websocket = websocket
        if callable(self.__init):
            await self.__init()

        for event_name in event.EventName_LIST:
            message = event.get_event_request(event_name)
            await websocket.send(message)

        async for msg in websocket:
            message = json.loads(msg)
            await self.parse_message(message)

    async def __start(self, host: str, port: int):
        async with websockets.serve(self.receive, host, port):
            await asyncio.Future()

    async def run_command(self, cmd: str) -> dict:
        message = command.get_command_request(cmd)
        await self.websocket.send(message)
        result = {}
        async for msg in self.websocket:
            responce = json.loads(msg)
            messagePurpose = responce['header']['messagePurpose']

            if messagePurpose == 'commandResponse' or messagePurpose == 'error':
                result = responce
                break

        return result

    async def tell(self, msg: str, selector: str = "@a") -> dict:
        return await self.run_command(f"tell {selector} {msg}")

    def start(self, host: str = "localhost", port: int = 7777):
        asyncio.run(self.__start(host, port))

    # TODO
    async def close(self):
        await self.websocket.close()

    def init(self, func):
        self.__init = func

    def listen(self, event: str = "all"):
        def _listen(func):
            self.__listener[event] = func
        return _listen
