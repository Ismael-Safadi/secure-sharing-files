
import os, random
from argparse import ArgumentParser, RawTextHelpFormatter

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import sys
global data
def onc():
    parser = ArgumentParser(
        usage='./%(prog)s -t [target] -p [port] -k [key] -f [file]',
        version="2",
        formatter_class=RawTextHelpFormatter,
        prog='sender',

    )
    options = parser.add_argument_group('options', '')
    options.add_argument('-d', metavar='<ip|domain>', default=False,
                         help='Specify your target such an ip or domain name')
    options.add_argument('-k', help='Set the encryption key ')
    options.add_argument('-p', metavar='<int>', help='Specify port target')
    options.add_argument('-f', metavar='<int>', help='Specify file target')
    args = parser.parse_args()
    if args.d == False:
        parser.print_help()
        sys.exit()
    IP = args.d
    PORT = args.p
    PORT = int(PORT)
    key = args.k
    print "IP:", IP
    print "port : ", PORT


    path =args.f
    from s import rsaencryptaes
    rsaencryptaes(key,IP)
    print "rsa done"
    key = SHA256.new(key)
    key = key.digest()
    chunk_size = 64 * 1024
    output_file = path + ".enc"
    file_size = str(os.path.getsize(path)).zfill(16)
    IV = ''
    for i in range(16):
        IV += chr(random.randint(0, 0xFF))
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    with open(path, 'rb') as inputfile:
        with open(output_file, 'wb') as outf:
            outf.write(file_size)
            outf.write(IV)
            while True:
                chunk = inputfile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                outf.write(encryptor.encrypt(chunk))
    print "encrypted done"
    from send_extention import sendd
    sendd(path, IP, PORT)

    print "done send extention"
    from server import res

    res(output_file,IP,PORT)

    print "Done ^__^ Your file is secure "

if __name__ == '__main__':
    onc()

