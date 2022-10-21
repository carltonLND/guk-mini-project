import os

PROMPT = """1) Yes
0) No
>>> """

product_list = []


def create(data):
    new_product = input("Enter Product Name:\n>>> ").strip()
    data.append(new_product)
    os.system("clear")
    return print(f"New Product #{len(data)}: {new_product}!\n")


def read(data):
    if not data:
        print("No Products Currently Available!")
        return False

    print("Products:")
    for index, product in enumerate(data, 1):
        print(f"{index}) {product.title()}")

    return True


def update(data):
    try:
        product_index = int(input("\nSelect Product To Update:\n>>> ")) - 1
    except ValueError:
        return print("Invalid Input!\n")

    if product_index > len(data) or product_index < 0:
        os.system("clear")
        return print("Invalid Input!\n")

    os.system("clear")
    new_product_name = input(f"Enter New Product Name:\n>>> ").strip()
    os.system("clear")
    print(f"Update '{data[product_index]}' -> '{new_product_name}'?\n")
    confirmation = input(PROMPT).lower()

    if confirmation == "0":
        return os.system("clear")

    if confirmation == "1":
        data[product_index] = new_product_name
        os.system("clear")
        return print("Product Name Updated!\n")

    os.system("clear")
    return print(f"'{confirmation}' Is Not A Valid Command!\n")


def delete(data):
    try:
        product_index = int(input("\nSelect Product To Delete:\n>>> ")) - 1
    except ValueError:
        return print("Invalid Input!\n")

    if product_index > len(data) or product_index < 0:
        os.system("clear")
        return print("Invalid Input!\n")

    os.system("clear")
    print(f"Delete '{data[product_index]}'?\n")
    confirmation = input(PROMPT).lower()

    if confirmation == "0":
        return os.system("clear")

    if confirmation == "1":
        data.pop(product_index)
        os.system("clear")
        return print("Product Deleted!")

    os.system("clear")
    return print(f"'{confirmation}' Is Not A Valid Command!\n")
