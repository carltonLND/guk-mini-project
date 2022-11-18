from dataclasses import dataclass, field


@dataclass
class Courier:
    """Courier dataclass"""

    id: int = field(init=False)
    name: str
    phone: int
