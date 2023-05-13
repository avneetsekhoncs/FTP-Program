import socket

HOST = socket.gethostbyname(socket.gethostname())       #Public network interface
PORT = 50007                                            #Arbritary port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Address family, socket type
print(f"[+] Connecting to {HOST}:{PORT}")

s.connect((HOST, PORT))                                 #Connect to remote socket at address
print("[+] Connected to ", HOST)