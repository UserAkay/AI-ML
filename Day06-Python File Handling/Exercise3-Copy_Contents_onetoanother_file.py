def copy_file(src, dest):
    try:
        with open(src, "r") as source_file:
            content = source_file.read()

        with open(dest, "w") as dest_file:
            dest_file.write(content)

        print(f"Contents copied from '{src}' to '{dest}' successfully.")
    except FileNotFoundError:
        print(f"File '{src}' not found!")


source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")
copy_file(source, destination)
