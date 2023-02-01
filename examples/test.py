import wsminepy as ws
from wsminepy.agent import Agent
from wsminepy.mcdata import Direction as D
from wsminepy.mcdata import TurnDirection as TD

if __name__ == '__main__':
    server = ws.Server()
    agent = Agent(server)

    @server.init
    async def start():
        print(await agent.create())

    @server.listen(event="PlayerMessage")
    async def playerMessage(data):
        msg = data['message']
        sender = data['sender']
        print(f"<{sender}>{msg}")

        if msg == "#test":
            for i in range(1, 10):
                print(i)
                print(await agent.move(D.Left))
        elif msg == "#kill":
            await server.run_command("kill @e[type=agent]")
        elif msg == "#close":
            await server.close()
    server.start()
