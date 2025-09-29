import os
import shutil

fldr = input("Enter the folder path you wish to organize:")
files = os.listdir(fldr)

for index, file in enumerate(files, start=1):      
    old = os.path.join(fldr, file)
    name, extension = os.path.splitext(file)
    new = os.path.join(fldr, f"file{index}{extension}")
    os.rename(old, new)

for file in os.listdir(fldr):
    name, extension = os.path.splitext(file)

    if extension == ".txt":
        d_fldr = os.path.join(fldr, "txt_files")
    elif extension == ".jpg":
        d_fldr = os.path.join(fldr, "images")
    else:
        d_fldr = os.path.join(fldr, "others")

    os.makedirs(d_fldr, exist_ok=True)
    shutil.move(os.path.join(fldr, file), os.path.join(d_fldr, file))