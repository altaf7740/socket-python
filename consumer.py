import socket
import threading
from config import bcolors, SERVER, PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

def send_msg():
    while True:
        sock.send(input("").encode())

def get_msg():
    while True:
        try:
            data= sock.recv(1024).decode("ascii") 
            print(f"{bcolors.OKBLUE}>>> {data}{bcolors.ENDC}")
        except:
            sock.close()

threading.Thread(target=get_msg).start()
threading.Thread(target=send_msg).start()