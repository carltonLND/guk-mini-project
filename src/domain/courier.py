class Courier:
    def __init__(self, name: str, phone: int, id: int | None = None) -> None:
        self.name = str(name)
        self.phone = int(phone)
        if id == None:
            self.id = id
        else:
            self.id = int(id)
