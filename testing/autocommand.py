import socket
import time

TCP_IP = '192.168.1.12'
TCP_PORT = 1234
BUFFER_SIZE = 8

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

for x in xrange(0, 1000):
	time.sleep(0.0005)
	s.send('AT!MTR_CMD=GOTO,5,5')
	data = s.recv(BUFFER_SIZE)
	print "received:", data


s.close()

