#!/usr/bin/env python

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util import randpool
import pickle
import socket
def rsaencryptaes(aeskey,host):
    port=50002
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((host, port))
            break
        except:
            continue
    rcstring = s.recv(2048)
    publickey = pickle.loads(rcstring)
    secretText = publickey.encrypt(aeskey, 32)
    s.sendall(pickle.dumps(secretText))
    s.close()

