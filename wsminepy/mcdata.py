from dataclasses import dataclass
from enum import Enum


class Color:
    Black = "§0"
    DarkBlue = "§1"
    DarkGreen = "§2"
    LightBlue = "§3"
    DarkRed = "§4"
    DarkPurple = "§5"
    Gold = "§6"
    Gray = "§7"
    DarkGray = "§8"
    Blue = "§9"
    Green = "§a"
    SkyBlue = "§b"
    Red = "§c"
    Pink = "§d"
    Yellow = "§e"
    White = "§f"


class Dimention(Enum):
    Overworld = 0
    Nether = 1
    TheEnd = 2


class Direction(Enum):
    Forward = "forward"
    Back = "back"
    Left = "left"
    Right = "right"
    Up = "up"
    Down = "down"


class TurnDirection(Enum):
    Left = "left"
    Right = "right"


@dataclass
class Player:
    color: str
    dimension: Dimention
    id: int
    name: str
    position: tuple[float, float, float]
    type: str
    variant: int
    yRot: float


@dataclass
class Block:
    aux: int
    id: str
    namespace: str

