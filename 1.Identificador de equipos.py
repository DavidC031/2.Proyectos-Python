import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print ("El nombre de computador es: " + hostname)
print ("La ip del computador es:" + ip)