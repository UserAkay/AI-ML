def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")

def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print("Items in the file:")
            for item in items:
                print(item.strip())

    except FileNotFoundError:
        print(f"file {filename, "r"} not found!")

fruits = ["Apple", "Banana", "Cherry", "Grapes"]
write_item_to_file("fruits.txt", fruits)
read_items_from_file("fruits.txt")