import os

cwd = os.getcwd()
data_dir = os.path.join(cwd, "data/")


def format_txt_data():
    flist = list(filter(lambda x: x.endswith(".txt"), os.listdir(data_dir)))
    for file in flist:
        with open(os.path.join(cwd, f"data/{file}"), "r") as f:
            lines = f.readlines()

        with open(os.path.join(cwd, f"data/{file}"), "w") as f:
            for line in lines:
                if line.isspace():
                    pass
                else:
                    f.write(line)


def get_txt_data(file):
    flist = list(filter(lambda x: x.endswith(".txt"), os.listdir(data_dir)))
    findex = flist.index(f"{file}")
    if not file:
        return False

    with open(os.path.join(os.getcwd(), f"data/{flist[findex]}"), "r") as f:
        for count, line in enumerate(f.readlines(), 1):
            yield f"{count}) {line.strip().title()}"


def add_txt_data(file, new_entry):
    flist = list(filter(lambda x: x.endswith(".txt"), os.listdir(data_dir)))
    findex = flist.index(f"{file}")
    if not file:
        return False

    with open(os.path.join(cwd, f"data/{flist[findex]}", "w")) as f:
        f.write(f"\r{new_entry}")
