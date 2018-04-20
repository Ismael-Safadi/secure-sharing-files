from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)


def sendd(sender,host,port):
    host =host
    port =port
    while True:
        try:
            s.connect((host, port))
            break
        except:
            continue

    sender = sender.encode('utf-8')
    s.send(sender)
    s.close()
