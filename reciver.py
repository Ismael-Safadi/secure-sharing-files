from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import time
import threading 
from argparse import ArgumentParser,RawTextHelpFormatter
import sys



global Name
global IP
global PORT

def receive():
    parser = ArgumentParser(
        usage='./%(prog)s -t [target] -p [port] -k [key]',
        version="2",
        formatter_class=RawTextHelpFormatter,
        prog='reciver',

    )
    options = parser.add_argument_group('options', '')
    options.add_argument('-d', metavar='<ip|domain>', default=False,
                         help='Specify your target such an ip or domain name')
    options.add_argument('-k', help='Set the encryption key ')
    options.add_argument('-p', metavar='<int>', help='Specify port target')


    args = parser.parse_args()
    if args.d == False:
        parser.print_help()
        sys.exit()
    IP = args.d
    PORT = args.p
    PORT = int(PORT)
    KEA = args.k
    global finalfilename
    from r import rsadecyptaes
    keyy = rsadecyptaes(IP)
    print keyy
    print (type(keyy))
    from resiver_extention import extention
    path = extention(IP, PORT)
    finalfilename = "securefile" + path + ".enc"
    print finalfilename
    from client1 import sen
    sen(finalfilename,IP,PORT)
    if keyy != KEA:
        print "the key doesnt correct , try again "
        sys.exit()
    #tm.showinfo(title="Done", message="Receiving Done ^__^ Your file is secure ")
    key = SHA256.new(keyy)
    key = key.digest()

    chunk_size = 64 * 1024
    output_file = finalfilename[:-4]
    with open(finalfilename, 'rb') as inf:
        filesize = long(inf.read(16))
        IV = inf.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        with open(output_file, 'wb') as outf:
            while True:
                chunk = inf.read(chunk_size)
                if len(chunk) == 0:
                    break
                outf.write(decryptor.decrypt(chunk))
            outf.truncate(filesize)

threading.Thread(target=receive).start()
print "listening started"
