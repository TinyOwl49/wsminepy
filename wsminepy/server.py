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

    async def receive(self, websocket: WebSocketServerProtocol, path: str):
        self.websocket = websocket
        if callable(self.__init):
            await self.__init()

        for event_name in event.EventName_LIST:
            message = event.get_event_request(event_name)
            await websocket.send(message)

        async for msg in websocket:
            message = json.loads(msg)
            await self.parse_message(message)

    async def __start(self):
        async with websockets.serve(self.receive, "localhost", 7777):
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

    def start(self):
        asyncio.run(self.__start())

    # TODO
    async def close(self):
        await self.websocket.close()

    def init(self, func):
        self.__init = func

    def listen(self, event: str = "all"):
        def _listen(func):
            self.__listener[event] = func
        return _listen


# if __name__ == '__main__':
#     server = Server()

#     @server.init
#     def start():
#         print("connect")

#     @server.listen(event="PlayerMessage")
#     async def playerMessage(data):
#         msg = data['message']
#         sender = data['sender']
#         print(f"<{sender}>{msg}")

#         if msg == "#hoge":
#             result = await server.tell(f"{Color.Red}hoge{Color.Pink}hoge")
#             print(f"{Color.Red}hoge{Color.Pink}hoge")
#             print(result)
#         elif msg == "#test":
#             result = await server.run_command("kill @e[type=!player]")
#             print(result)

#     @server.listen(event="MobKilled")
#     async def mobKilled(data):
#         print(data)

#     @server.listen(event="MenuShown")
#     async def menuShown(data):
#         print(data)

#     @server.listen(event="EntitySpawned")
#     async def entitySpawned(data):
#         print(data)

#     server.start()
