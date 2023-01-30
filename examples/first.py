import wsminepy as ws
from wsminepy.mcdata import Color

if __name__ == '__main__':
    server = ws.Server()

    @server.init
    def start():
        print("connect")

    # show event list
    # from wsminepy import event
    # print(event.EventName_LIST)

    # listen event in minecraft
    # default: listen all events
    @server.listen()
    async def allEvent(data):
        print("event")

    @server.listen(event="PlayerMessage")
    async def playerMessage(data):
        msg = data['message']
        sender = data['sender']
        print(f"<{sender}>{msg}")

        if msg == "#hoge":
            result = await server.tell(f"{Color.Red}hoge{Color.Pink}hoge")
            print(f"{Color.Red}hoge{Color.Pink}hoge")
            print(result)
        elif msg == "#test":
            result = await server.run_command("kill @e[type=!player]")
            print(result)

    @server.listen(event="MobKilled")
    async def mobKilled(data):
        print("mobKilled: ", data)

    @server.listen(event="EntitySpawned")
    async def entitySpawned(data):
        print(data)

    server.start()
