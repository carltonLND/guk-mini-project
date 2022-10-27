import file_handlers.txt as txt


def handler(file):
    supported_extensions = [".txt"]
    extension = file[-4:]
    if extension not in supported_extensions:
        raise Exception("ERROR: File Type Not Supported!")

    return extension


def create_data(file, new_entry, multi=False):
    file_type = handler(file)
    if multi:
        if file_type == ".txt":
            return txt.add_multi_data(file, new_entry)

    if file_type == ".txt":
        return txt.add_file_data(file, new_entry)


def get_data(file, multi=False):
    file_type = handler(file)
    if multi:
        if file_type == ".txt":
            return txt.get_multi_data(file)

    if file_type == ".txt":
        return txt.get_file_data(file)


def update_data(file, old_name, new_name):
    file_type = handler(file)
    if file_type == ".txt":
        return txt.update_file_data(file, old_name, new_name)


def delete_data(file, data_to_delete):
    file_type = handler(file)
    if file_type == ".txt":
        return txt.delete_file_data(file, data_to_delete)
