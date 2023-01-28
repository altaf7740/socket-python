import socket
import threading
from config import bcolors, SERVER, PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((SERVER, PORT))
sock.listen(2)
conn, addr = sock.accept()

def send_msg():
    while True:
        conn.send(input("").encode())


def get_msg():
    while True:
        try:
            data= conn.recv(1024).decode("ascii") 
            print(f"{bcolors.OKBLUE}>>> {data}{bcolors.ENDC}")
        except:
            conn.close()


threading.Thread(target=get_msg).start()
threading.Thread(target=send_msg).start()