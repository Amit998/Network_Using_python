import threading
import socket

host='127.0.0.1'

port = 55555


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()


clients=[]
nicknames=[]


def broadcast(message):
    for client in clients:
        client.send(message)



def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=client.index(client)
            clients.remove(client)
            clients.close()
            nickname=nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client,address=server.accept()
        print(f"Connected With {str(address)}")

        client.send('Nick'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        nicknames.append(client)


        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} join the chat".encode('ascii'))
        client.send('Connected to th server!'.encode('ascii'))

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()


print("Server is Listning")
receive()