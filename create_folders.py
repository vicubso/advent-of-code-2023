import os
import sys

def create_folders(a, b):

    with open('template.txt', 'r') as file:
        template = file.read()

    for i in range(a, b+1):
        folder_name = f"day-{i}"
        os.makedirs(folder_name, exist_ok=True)
        file_name = f"{folder_name}/day-{i}.py"
        contents = template.format(i=i)
        with open(file_name, 'w') as file:
            file.write(contents)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_folders.py <a> <b>")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    create_folders(a, b)






