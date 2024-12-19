import os

fold = input("please give me you folder input").split()

for folder in fold:
    files = os.listdir(folder)
    print(files)