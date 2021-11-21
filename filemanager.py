# # # # Project Name : Auto File Organization
# # # # Name : Awadhesh Gupta
# # # # Enrollment No. : 20SOECE11095
# # # # Class : 3CEC

import os, shutil
from os.path import join

path = input("Enter the path: ")

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(join(path, extension)):
        shutil.move(join(path, file), join(path, extension, file))
    else:
        os.makedirs(join(path, extension))
        shutil.move(join(path, file), join(path, extension, file))
