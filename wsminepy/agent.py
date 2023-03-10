from wsminepy.mcdata import Direction, TurnDirection
from wsminepy.server import Server


class Agent(object):
    def __init__(self, server: Server) -> None:
        self.server = server

    async def create(self):
        return await self.server.run_command("agent create")

    async def move(self, direction: Direction):
        return await self.server.run_command(f"agent move {direction.value}")

    async def turn(self, direction: TurnDirection):
        return await self.server.run_command(f"agent turn {direction.value}")

    async def attack(self, direction: Direction):
        return await self.server.run_command(f"agent attack {direction.value}")

    async def destroy(self, direction: Direction):
        return await self.server.run_command(f"agent destroy {direction.value}")

    async def drop(self, slotNum: int, quantity: int, direction: Direction):
        return await self.server.run_command(f"agent drop {slotNum} {quantity} {direction.value}")

    async def dropall(self, direction: Direction):
        return await self.server.run_command(f"agent dropall {direction.value}")

    async def inspect(self, direction: Direction):
        return await self.server.run_command(f"agent inspect {direction.value}")

    async def inspectdata(self, direction: Direction):
        return await self.server.run_command(f"agent inspectdata {direction.value}")

    async def detect(self, direction: Direction):
        return await self.server.run_command(f"agent detect {direction.value}")

    async def detectredstone(self, direction: Direction):
        return await self.server.run_command(f"agent detectredstone {direction.value}")

    async def transfer(self, srcSlotNum: int, quantity: int, dstSlotNum: int):
        return await self.server.run_command(f"agent transfer {srcSlotNum} {quantity} {dstSlotNum}")

    async def tpagent(self):
        return await self.server.run_command(f"agent tpagent")

    async def collect(self, item: str):
        return await self.server.run_command(f"agent collect {item}")

    async def till(self, direction: Direction):
        return await self.server.run_command(f"agent till {direction.value}")

    async def place(self, slotNum: int, direction: Direction):
        return await self.server.run_command(f"agent place {slotNum} {direction.value}")

    async def getitemcount(self, slotNum: int):
        return await self.server.run_command(f"agent getitemcount {slotNum}")

    async def getitemspace(self, slotNum: int):
        return await self.server.run_command(f"agent getitemspace {slotNum}")

    async def getitemdetail(self, slotNum: int):
        return await self.server.run_command(f"agent getitemdetail {slotNum}")
