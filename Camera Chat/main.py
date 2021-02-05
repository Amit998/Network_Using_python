from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

receving=StreamingServer('172.0.144.1',9999)
sending=CameraClient('172.0.144.1',9999)

t1=threading.Thread(target=receving.start_server)
t1.start()

time.sleep(2)

t2=threading.Thread(target=receving.start_server)
t2.start()

while input("") !='STOP':
    continue

receving.start_server()
sending.start_stream()