import socket
import os
import tqdm


HOST = socket.gethostbyname(socket.gethostname())       #Public network interface
PORT = 50007                                            #Arbritary port number
BUF_SIZE = 4096                                      #Maximum anount of data received at once
SPLIT = "<SPLIT>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Address family, socket type
s.bind((HOST, PORT))                                        #Bind the socket to the host at the specified port
s.listen(10)                                                #10 specifies the number of unaccepted connection before refusing new connections

print(f"[*] Listening as {HOST}:{PORT}")
print("Waiting for the client to connect... ")

conn, addr = s.accept()                                     #Accept a connection
print(f"[+] {addr} is connected.")

r = conn.recv(BUF_SIZE).decode()                            #Translate received data
filename, filesize = r.split(SPLIT)                         #Split received data into filename and filesize
filename = os.path.basename(filename)
filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f"Downloading {filename}", unit="B", unit_scale = True, unit_divisor = 1024)        #"B" = specified units BYTES, unit_scale = use scaled units instead og just bytes KB MB GB, unit_divisor = divisor used to calculate scaled unit

with open(filename, "wb") as file:                      #open file for writing in binary mode
    while True:
        bytes_downloaded = conn.recv(BUF_SIZE)          #get data of specified size
        if bytes_downloaded == b'':                        #break if empty bytes object is returned
            break
        file.write(bytes_downloaded)
        progress.update(len(bytes_downloaded))          #update progress bar

conn.close()                #close connection
s.close()                   #close socket