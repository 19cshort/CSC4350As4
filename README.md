# CSC4350As4
http server with socket

Description: The client will reach out to the server and ask for specific information determined by the user. The client is a web browser which will reach out to the server and make use of the GET http request to return and show a file of the user's choice. The user will open a web browser and type 'http://127.0.0.1:portNumber/resourseRequested' (with the portNumber being the port the server is listening on and resourseRequested being the file the user requests from the server) this will either return the resourse requested or return a 404 if the resourse is not found. Also, if no resourse is specified in the request the server will return a default file called 'index.html'.

New features: there is a logging feature added to the server with this format: host(ip of client) ident authuser date request status bytes User_Agent. The ident and authuser are just represented as dashes. Error pages, there is now a visible error shown to the user if they request a resource that the server does not have access to and if there is a non get request with the error messages looking like: "ERROR 400: BAD REQUEST" and "ERROR 404: ITEM NOT FOUND" respectively. There is also now a server identifier added in the response headers which looks like: "Server: cool webserver".

I ran the server on a windows machine and requested resources from it from Google Chrome

Instruction for execution and command line flags: I ran this on python version 3.9.4 I opened an IDLE for the server and opened it from the IDLE. The server REQUIRES the -p commandline parameter and is done so by doing -p 8000 for example (where 8000 can be replaced with the port of your choice)

Command line parameters: the -h command can be used to bring up a couple of help messages. the -p command will specify the port number for the server to be listening on. The -p is required and if none is provided the program will exit with a message. To use the -p command type '-p 8000' for example to specify 8000 as the port number for the server to be listening on.

Notes: There is an interesting error that happens if the server sits open and idle (i.e. no requests being sent to it) for ~3 minutes. It seems that it tries to parse another request with the splits I have, but since there is no actual request it errors out. I tried sending a 'Connection: closed' response header and this did not fix the issue. I also added two files along with the source code for testing purposes.
