def create(data: list[str], new_product: str) -> None:
    data.append(new_product)


def read(data: list[str]) -> bool:
    if not data:
        print("No Products Currently Available!\n")
        return False

    print("Products:")
    for index, product in enumerate(data, 1):
        print(f"{index}) {product.title()}")

    print()
    return True


def update(data: list[str], old_product: int, new_product: str) -> None:
    data[old_product] = new_product


def delete(data: list[str], product_index: int) -> None:
    data.pop(product_index)
