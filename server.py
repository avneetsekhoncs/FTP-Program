import socket

HOST = socket.gethostbyname(socket.gethostname())       #Public network interface
PORT = 50007                                            #Arbritary port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Address family, socket type
s.bind((HOST, PORT))                                        #Bind the socket to the host at the specified port
s.listen(10)                                                #10 specifies the number of unaccepted connection before refusing new connections

print(f"[*] Listening as {HOST}:{PORT}")
print("Waiting for the client to connect... ")

while True:
    conn, addr = s.accept()                                     #Accept a connection
    print(f"[+] {addr} is connected.")



