from dataclasses import dataclass

@dataclass
class Cell:
    y: int
    x: int
    val: str
    visible: bool

    