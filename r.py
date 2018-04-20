#!/usr/bin/env python
# generate the RSA key
from Crypto.PublicKey import RSA
from Crypto.Util import randpool
import pickle
import socket
def rsadecyptaes(hostt):
    host=hostt
    port=50002
    blah = randpool.RandomPool()
    RSAKey = RSA.generate(1024, blah.get_bytes)
    RSAPubKey = RSAKey.publickey()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    clientsock, clientaddr = s.accept()
    clientsock.send(pickle.dumps(RSAPubKey))
    rcstring = ''
    buf = clientsock.recv(1024)
    rcstring += buf
    clientsock.close()
    encmessage = pickle.loads(rcstring)
    key = RSAKey.decrypt(encmessage)
    s.close()
    return key

