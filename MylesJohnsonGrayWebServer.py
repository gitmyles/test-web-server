#Myles Johnson-Gray
#Networking Project #3
#Due March 5, 2015

from socket import *

#Prepare a server socket
serverPort = 1025
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is now ready to take requests.")

#Server is waiting for requests
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Handling request...")
    #Read request msgs into a file to be read later
    cFile = open('connectionFile.txt', 'rb+')
    try:
        sentence = connectionSocket.recv(1024)
        cFile.write(sentence)
        cFile.close()

        #Open connection file and extract information
        cFile = open('connectionFile.txt', 'rb')
        message = cFile.read()
        filename = message.decode('utf-8').split(" ")[1]
        httpVersion = message.decode("latin1").split(" ")[2].split("\n")[0]
        print(filename)
        httpVersion.encode('utf-8')

        #Send one HTTP header line into socket
        responseHeader = 'HTTP/1.1 200 OK\n\n'
        connectionSocket.send(bytes(responseHeader, 'utf-8'))

        #Open file data and send across connection
        f = open(filename[1:], 'rb')
        connectionSocket.send(f.read())

    #Send response message for file not found
    except IOError as e:
        print(e)
        connectionSocket.send(bytes('HTTP/1.1 404 Not Found\n\n', 'utf-8'))

connectionSocket.close()
serverSocket.close()
cFile.close
