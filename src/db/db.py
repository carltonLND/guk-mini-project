import os
from typing import final

from file_handlers.txt import add_txt_data, get_txt_data

def handler(file):
    supported_extensions = [".txt"]
    extension = file[-4:]
    if extension not in supported_extensions:
        return print("File Type Not Supported!")

    return extension


def create_data(file, new_entry):
    return add_txt_data(file, new_entry)


def get_data(file):
    file_type = handler(file)
    if file_type == ".txt":
        return get_txt_data(file)
    return


def update_data(old_element: int, new_element):
    data[old_element] = new_element


def delete_data(element_index: int):
    data.pop(element_index)
