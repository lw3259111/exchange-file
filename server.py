import socket
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("172.17.14.34",9999))
    sock.listen(10)
    while True:
        connection,address = sock.accept()
        try:
            #connection.settimeout(5)
            fl = ''
            buf = connection.recv(4096)
            print buf
            """while buf:
                fl += buf
                buf = connection.recv(1024)
                print fl
            """
            f = open(buf,'rb')
            fout = f.read()
            #while fout:
            connection.sendall(fout)
            f.close()
        except socket.timeout:
            print 'time out'
        connection.close()
    sock.close()
