import wsminepy as ws
from wsminepy.agent import Agent
from wsminepy.mcdata import Direction

if __name__ == '__main__':
    server = ws.Server()
    agent = Agent(server)

    @server.init
    async def start():
        res, head = await agent.create()
        print("[system]", res.statusMessage)
        print("[status]", res.statusCode)

    @server.listen(event="PlayerMessage")
    async def playerMessage(data):
        msg = data['message']
        sender = data['sender']
        print(f"<{sender}>{msg}")

        if msg == "#test":
            for _ in range(1, 10):
                res, h = await agent.move(Direction.Left)
                print("[system]", res.statusMessage)
        elif msg == "#kill":
            res, _ = await server.run_command("kill @e[type=agent]")
            print(res.statusMessage)
        elif msg == "tp":
            print((await agent.tpagent())[0].statusMessage)
        elif msg == "#close":
            await server.close()
        elif msg == "pos":
            res, h = await server.run_command("agent getposition")
            print(res.statusMessage)
    server.start()
