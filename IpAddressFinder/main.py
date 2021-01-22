import socket
from  requests import get


hostname=socket.gethostname()
localIP=socket.gethostbyname(hostname)
publicIP=get('https://api.ipify.org').text


print(f"Hostname :{hostname}")
print(F"Local IP Address : {localIP}")

print(F"Publi IP Address : {publicIP}")