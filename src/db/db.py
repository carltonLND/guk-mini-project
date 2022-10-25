import os

from file_handlers.txt import (
    add_txt_data,
    delete_txt_data,
    get_txt_data,
    update_txt_data,
)


def handler(file):
    supported_extensions = [".txt"]
    extension = file[-4:]
    if extension not in supported_extensions:
        raise Exception("ERROR: File Type Not Supported!")

    return extension


def create_data(file, new_entry):
    file_type = handler(file)
    if file_type == ".txt":
        return add_txt_data(file, new_entry)


def get_data(file):
    file_type = handler(file)
    if file_type == ".txt":
        return get_txt_data(file)
    return


def update_data(file, old_name, new_name):
    file_type = handler(file)
    if file_type == ".txt":
        return update_txt_data(file, old_name, new_name)


def delete_data(file, data_to_delete):
    file_type = handler(file)
    if file_type == ".txt":
        return delete_txt_data(file, data_to_delete)
