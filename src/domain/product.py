from dataclasses import dataclass, field


@dataclass
class Product:
    """Product dataclass"""

    id: int = field(init=False)
    name: str
    price: float
