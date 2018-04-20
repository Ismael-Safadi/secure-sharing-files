import socket
import sys
def res(filename,hostt,portt):
    port = portt
    s = socket.socket()
    host = hostt
    s.bind((host, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        f = open(filename,'rb')
        l = f.read()
        while (l):
           conn.send(l)
           l = f.read()
        f.close()
        conn.close()
        print "Done ^__^ Your file is secure "
        sys.exit()
