from socket import *
serverport = 12000
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(('', serverport))
print("the server is ready to receive")
while True:
    message, clientAddress = serversocket.recvfrom(2048)
    modifyedMessage = message.decode().upper()
    serversocket.sendto(modifyedMessage.encode(), clientAddress)
