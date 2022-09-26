# CSC4350As4
http server with socket

Description: The client will reach out to the server and ask for specific information determined by the user. The client is a web browser which will reach out to the server and make use of the GET http request to return and show a file of the user's choice. The user will open a web browser and type 'http://127.0.0.1:portNumber/resourseRequested' (with the portNumber being the port the server is listening on and resourseRequested being the file the user requests from the server) this will either return the resourse requested or return a 404 if the resourse is not found. Also, if no resourse is specified in the request the server will return a default file called 'index.html'.

Instruction for execution and command line flags: I ran this on python version 3.9.4 I opened an IDLE for the server and opened it from the IDLE

Command line parameters: the -h command can be used to bring up a couple of help messages. the -p command will specify the port number for the server to be listening on. The -p is required and if none is provided the program will exit with a message. To use the -p command type '-p 8000' for example to specify 8000 as the port number for the server to be listening on.

Notes: There is an interesting error that will happen server side sometimes where the program will error out saying that no request has been sent. this has only happened a time or two and I'm not able to recreate it on command so I'm not sure what's going on there. I also added two files along with the sourse code for testing purposes
