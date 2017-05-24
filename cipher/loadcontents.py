def load_sheet(filename) :
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents
