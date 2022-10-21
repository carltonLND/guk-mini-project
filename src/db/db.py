def create(data, new_product):
    return data.append(new_product)


def read(data):
    if not data:
        print("No Products Currently Available!\n")
        return False

    print("Products:")
    for index, product in enumerate(data, 1):
        print(f"{index}) {product.title()}")

    print()
    return True


def update(data, old_product, new_product):
    data[old_product] = new_product


def delete(data, product_index):
    data.pop(product_index)
