from socket import socket, AF_INET, SOCK_STREAM
import os


def extention(host,port):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    c, a = s.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break;
        else:
            data = data.replace(".enc", "")
            fname, fextention = os.path.splitext(data)

    c.close()

    return fextention
