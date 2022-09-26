#Connor Short
#python version 3.9.4
#open an IDLE shell and run the server
#used the socket library for the tcp socket, used optparse to get commandline parameters, used os and sys libraries to check if a requested file is available

from socket import *
import socket
from optparse import OptionParser
import os
import sys


#options for command line parameters
parser = OptionParser()
parser.add_option("-p",
                  action = "store", type = "int", dest = "serverPort", default = 99999999,
                  help = "choose the port for the server to listen on")
parser.add_option("-r",
                  help = "open a python IDLE and run the server so that command line parameters are accepted" + '\n' + "use the -p parameter to specify a port (e.g. -p 8000) (this is requred)" + '\n' + "open a browser and type 'http://127.0.0.1:8000/index.html' with the 8000 being your selected port number and the index.html being your requested file")

(options, args) = parser.parse_args()

#if statement to enusure a port was specified and if it was specified that it is valid
if options.serverPort == 99999999:
    print ("please be sure to spefiy a port for the server to run on")

elif options.serverPort > 65535 or options.serverPort < 1:
    print ("please be sure to specify a VALID port number")

else:
    serverSocket = socket.socket(AF_INET, SOCK_STREAM) #creating the socket
    serverSocket.bind(('127.0.0.1',options.serverPort)) #binding it to the chosen port and the loopback address
    serverSocket.listen(1)
    print ("The server is ready to recieve")

    while True:
        connectionSocket, clientAddress = serverSocket.accept()
        message = connectionSocket.recv(2048) #recieving the http request
        modifiedMessage = message.decode()
        request = modifiedMessage.split('\r\n',1) #splitting the message so that the first line of the request is in request [1]
        requestType, fileRequested, httpVersion = request[0].split() #splitting the topline into its parts

        #if statement so that if no filel is requested then index.html is returned
        if fileRequested == "/":
            fileRequested = "index.html"

        if fileRequested[0] == '/':
            fileRequested = fileRequested.replace('/', '') #removing the / at the beginning of the file
        print (fileRequested)

        accessAvailable = os.access(fileRequested, os.R_OK) #checking if the requested file is available for reading

        #if statement on whether or not the file is accessable
        if accessAvailable == True:
            file = open(fileRequested, "r") #opening the requested file for reading
            outputData = file.readlines() #reading all lines of the file and storing them in outputData

            responseLine = httpVersion + ' ' + '200' + ' ' + 'OK' + '\r\n' + '\r\n' #creating the top line of the http respnse (200)
            connectionSocket.send(responseLine.encode()) #sending the top line of the http response

            #for loop to send all of output data 
            for i in range(0, len(outputData)):
                connectionSocket.send(outputData[i].encode())

            connectionSocket.send("\r\n".encode()) #final crlf sent

            file.close()

        else:
            responseLine = httpVersion + ' ' + '404' + ' ' + 'NOT FOUND' + '\r\n' + '\r\n' #reating the top line of the http response (404)
            connectionSocket.send(responseLine.encode()) #sending the top line of the http response
            outputData = "ERROR 404: ITEM NOT FOUND" #creating a message to be displayed to the user

            #for loop to send all of outputData through
            for i in range(0, len(outputData)):
                connectionSocket.send(outputData[i].encode())

            connectionSocket.send("\r\n".encode()) #final crlf sent
