import os
import pathlib

data_dir = os.path.join(
    pathlib.Path(os.path.dirname(__file__)).parent.parent.absolute(), "data/"
)
txt_files = list(filter(lambda x: x.endswith(".txt"), os.listdir(data_dir)))


def format_txt_data():
    for file in txt_files:
        with open(data_dir + file, "r") as f:
            lines = f.readlines()

        with open(data_dir + file, "w") as f:
            for line in lines:
                if line.isspace():
                    pass
                else:
                    f.write(line)


def get_txt_data(file):
    if file not in txt_files:
        raise SystemExit(f"ERROR: {file} Not Found!")

    with open(data_dir + file, "r") as f:
        return [line.strip() for line in f.readlines()]


def get_multi_txt_data(file):
    if file not in txt_files:
        raise SystemExit(f"ERROR: {file} Not Found!")

    with open(data_dir + file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        orders = []
        start = 0
        stop = 4
        while stop <= len(lines):
            orders.append("\n   ".join(lines[start:stop]))
            start += 4
            stop += 4

    return orders


def add_txt_data(file, new_entry):
    if file not in txt_files:
        raise SystemExit(f"ERROR: {file} Not Found!")

    with open(data_dir + file, "a") as f:
        f.write(f"{new_entry}\n")

    return True


def add_multi_txt_data(file, new_entrys):
    if file not in txt_files:
        raise SystemExit(f"ERROR: {file} Not Found!")

    with open(data_dir + file, "a") as f:
        lines = []
        for key, value in new_entrys.items():
            lines.append(f"{key}: {value}\n")
        f.writelines(lines)


def update_txt_data(file, old_line, new_line):
    if file not in txt_files:
        raise SystemExit(f"ERROR: {file} Not Found!")

    with open(data_dir + file, "r") as f:
        lines = f.readlines()

    with open(data_dir + file, "w") as f:
        for count, line in enumerate(lines):
            if count == old_line:
                f.write(line.replace(line, f"{new_line}\n"))
            else:
                f.write(line)

    format_txt_data()
    return True


def delete_txt_data(file, data_to_delete):
    if file not in txt_files:
        raise SystemExit(f"ERROR: {file} Not Found!")

    with open(data_dir + file, "r") as f:
        lines = f.readlines()

    with open(data_dir + file, "w") as f:
        for count, line in enumerate(lines):
            if count == data_to_delete:
                pass
            else:
                f.write(line)

    format_txt_data()
    return True
