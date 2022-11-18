from dataclasses import dataclass, field
from enum import Enum, auto


class Status(Enum):
    PREPARING = "Preparing"
    ON_THE_WAY = "On the way"
    DELIVERED = "Delivered"


@dataclass
class Order:
    """Order dataclass"""

    id: int = field(init=False)
    customer_name: str
    customer_address: str
    customer_phone: int
    courier_id: int
    item_ids: str
    status: str = Status.PREPARING.value
