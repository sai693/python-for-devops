import os

folders = input("please give me you folder input").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name")
        break

    print("=== Listings file from the folders " +folder)

    for file in files:
        print(file)