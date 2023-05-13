import socket   #Socket interface
import os       #Operating system interfaces
import tqdm

SPLIT = "<SPLIT>"
BUF_SIZE = 4096                                      #Maximum anount of data received at once
HOST = socket.gethostbyname(socket.gethostname())       #Public network interface
PORT = 50007                                            #Arbritary port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Address family, socket type
print(f"[+] Connecting to {HOST}:{PORT}")

s.connect((HOST, PORT))                                 #Connect to remote socket at address
print("[+] Connected to ", HOST)

filename = input("Select file to transfer: ")           #User input
filesize = os.path.getsize(filename)                    #Get size of file at local path

s.send(f"{filename}{SPLIT}{filesize}".encode())     #Send the file over the connection and encode it to utf-8 format (default).

progress = tqdm.tqdm(range(filesize), f"Downloading {filename}", unit="B", unit_scale = True, unit_divisor=1024)        #"B" = specified units BYTES, unit_scale = use scaled units instead og just bytes KB MB GB, unit_divisor = divisor used to calculate scaled unit

with open(filename, "rb") as file:                      #open file for writing in binary mode
    while True:
        bytes_downloaded = file.read(BUF_SIZE)          #read data of specified size
        if bytes_downloaded == b'':                        #break if empty bytes object is returned
            break
        s.sendall(bytes_downloaded)
        progress.update(len(bytes_downloaded))          #update progress bar

s.close()                   #close socket