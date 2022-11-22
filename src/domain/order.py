from enum import Enum


class Order:
    def __init__(
        self,
        customer_name: str,
        customer_address: str,
        customer_phone: int,
        courier_id: int,
        item_ids: str,
        status: str = "1 (Preparing)",
        id: int | None = None,
    ) -> None:
        self.customer_name = str(customer_name)
        self.customer_address = str(customer_address)
        self.customer_phone = int(customer_phone)
        self.courier_id = int(courier_id)
        self.item_ids = str(item_ids)
        self.status = str(status)
        if id == None:
            self.id = id
        else:
            self.id = int(id)
