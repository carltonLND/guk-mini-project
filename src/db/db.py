from dataclasses import dataclass, field


@dataclass(kw_only=True, slots=True)
class Order:
    name: str
    address: str
    phone: int
    status: str = field(init=False, default="Preparing")


@dataclass(kw_only=True, slots=True)
class Product:
    name: str


@dataclass(kw_only=True, slots=True)
class Courier:
    name: str


@dataclass
class Data:
    orders: list[Order] = field(init=False, default_factory=list)
    products: list[Product] = field(init=False, default_factory=list)
    couriers: list[Courier] = field(init=False, default_factory=list)

    def read(self, data_type: str):
        try:
            return getattr(self, data_type)
        except AttributeError as e:
            print("ERROR:", e)

    def create_order(self, **kwargs):
        self.orders.append(Order(**kwargs))

    def create_product(self, **kwargs):
        self.products.append(Product(**kwargs))

    def create_courier(self, **kwargs):
        self.couriers.append(Courier(**kwargs))


db = Data()
