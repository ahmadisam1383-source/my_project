
import socket
import threading

host =None
port = None


clients = [] 


def broadcast(message, sender):
    for client,_ in clients:
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove((client,_))


def handle_client(client_socket):
    client_socket.send('enter your name'.encode('utf-8'))
    name =client_socket.recv(1024).decode('utf-8')
    clients.append((client_socket,name))
    welcome = f"{name} add in group"
    print(welcome)
    broadcast(welcome,client_socket)
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            full_messsage = f"{name} : {data}"
            print("📨📨",full_messsage)
            with open("history1.txt","a") as file:
                file.write(full_messsage+ "\n")

            broadcast(full_messsage, client_socket)
            client_socket.send('✔️✔️'.encode('utf-8'))
        except:
            break
    print(f"{name} قطع شد.")
    broadcast(f"{name}out of group",client_socket)
    clients.remove((client_socket, name))
    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(8)

print(f"🔵 سرور در حال گوش دادن روی پورت {port} است...")


while True:
    client_socket, _ = server.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()

