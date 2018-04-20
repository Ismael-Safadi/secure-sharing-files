# secure-sharing-files
secure sharing files using AES and RSA Algorithms 
<br>

# About
secure sharing files using AES and RSA Algorithms , Coded by : ismael Al-safadi 
<br> 
you can use this tool to share files securely , the file will encrypt by AES Algorithm  and the key of AES encryption will send to the anothe side
by RSA algorithm
<br>
# Using
first you need to install python , and the librarys 
<br>
1: Crypto
<br>
2: pickle
<br>
3:argparse
<br>
4: threading
<br>
then you need to run reciver on the reciver.py side before run the sender.py using this commend ./reciver.py -d [target] -p [port] -k [key]
<br> example >> python reciver.py -d 127.0.0.1 -p 8000 -k 1234
<br> after running reciver.py on the reciver side ,run the sender.py on sender side using this command ./sender -d [target] -p [port] -k [key] -f [file]
<br>
example ./sender.py -d 127.0.0.1 -p 8000 -k 1234 -f ./root/Desktop/image.png
<br>
note that  the ip ,port and key must be the same on the both side 
<br>
The ip must be the ip of reciver not the sender on the both side , thats mean if reciver ip is 10.10.10.12 and sender ip is 10.10.10.22
then you should put 10.10.10.12 on the both side 
<br>
to contact with me on facebook >> https://www.facebook.com/ismael.alsafadi
<br>
My email:ismaelalsafadi@protonmail.com
<br>
thank you for using my tool ^__^ 
<br>
