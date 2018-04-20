import socket
import sys
# Import socket module
def sen(filename,hostt ,portt):
    s = socket.socket()             # Create a socket object
    host = hostt    # Get local machine name
    port = portt                    # Reserve a port for your service.
    while True:
        try:
            s.connect((host, port))
            break
        except:
            continue


    with open(filename, 'wb') as f:

        while True:

            data = s.recv(1024)

            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    print('Successfully get the file')
    try:
        s.close()
    except:
        print "cant close the socket !!"
    

