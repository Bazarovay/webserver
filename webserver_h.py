import socket		#set up network connection
import os		#for command-line execution of php-cgi
import subprocess
import threading	#to permit concurrent client requests
import sys

#global variables from configuration file
doc_root=""
methods = ""
requests = ""
bad_requests = ""
ip_listen = ""
port = ""
#port = int(sys.argv[1])

#HOST --> HTTP header, HTTP_HOST --> ENV var for php-cgi
http_bash_map=[["Host","HTTP_HOST"], ["Accept","HTTP_ACCEPT"],["Aceept-Language","HTTP_ACCEPT_LANGUAGE"],["Accept-Encoding","HTTP_ACCEPT_ENCODING"],["Connection","HTTP_Connection"]]

#gets the requested file
def getFile(http_req):
	
	splitreq = http_req.split("\n")
	return splitreq[0].split(" ")[1]

#Gets the requested method
def getMethod(http_req):
	splitreq = http_req.split("\n")
	return splitreq[0].split(" ")[0]

#gets the HTTP Version
def getHTTPVersion(http_req):
	splitreq = http_req.split("\n")
	return splitreq[0].split(" ")[2]

def getHeaders(http_req):
	exportList = ""
	splitreq = http_req.split("\n")
	headernum = 1
	while (splitreq[headernum] != "\r"):
		headerparts = splitreq[headernum].split(":")
		for map in http_bash_map:
			if map[0] == headerparts[0]:
				exportList +="export %s='%s';" % (map[1],headerparts[1].strip('\r'))
		headernum = headernum + 1
	return exportList

def getVars(uri):
	uriparts = uri.split("?")
	return uriparts

def requestHandler(clientSock):
	request = clientSock.recv(2048)
	#get the requested method
	method = getMethod(request)
	version = getHTTPVersion(request)
	uriparts = getVars(getFile(request))
	elist = getHeaders(request)


	#send back error 505 if version is not 1.1 or 1.2
#	if (version == "HTTP/1.0") or (version == "HTTP/1.1") or (version == "HTTP/1.2"):
#		response = "HTTP/1.1 505 HTTP Version not supported"
#		footer = "\r\n\r\n"
#		clientSock.send(response+footer)
#		clientSock.close()

	
	#Close the socket if Connection is not keep-alive

	#Generate the php-cgi command
	runscript = "%s export REQUEST_METHOD='%s'; " % (elist,method)
	runscript = runscript + "export QUERY_STRING='%s'; " % (uriparts[1])
	runscript = runscript + "export SCRIPT_FILENAME='%s%s'; " % (doc_root,uriparts[0])
	runscript = runscript + " php-cgi -f %s%s" % (doc_root,uriparts[0])
	
	response = "HTTP/1.1 200 Ok\r\n"
	body = subprocess.check_output(runscript, shell=True)
	footer = "\r\n\r\n"
	full = response + body + footer
	clientSock.send(full)
	clientSock.close()

#define a function called main
def main():

	#define variables as global
	global port
	global ip_listen
	global methods
	global doc_root
	global requests
	global bad_requests

	#Get variables from the configuration file
	with open("webserver.conf") as f:
		config = []
		config = f.readlines()
		config = [item.strip() for item in config]
		config = [item.split(' ') for item in config]
		for item in config:
			if item[0] == "port":
				port = int(item[1])
			if item[0] == "ip_listen":
				ip_listen = item[1]
			if item[0] == "methods":
				methods = item[1]
			if item[0] == "doc_root":
				doc_root = item[1]
			if item[0] == "requests":
				requests = item[1]
			if item[0] == "bad_requests":
				bad_requests = item[1]


	#socket.socket is socket constructor
	#socket.AF_INET = ipv4
	#socket.SOCK_STREAM = use tcp not udp
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#.bind = make host listen, server side socket
	s.bind((ip_listen, port))
	try:
		#10 = number of concurrent connections possible
		s.listen(10)
		while True:
			#.accept() = establish a connection with a client
			#--> send syn/ack
			#blocking call
			(client_socket, client_addr) = s.accept()
			#target = request handler --> thread will run the function requestHandler
			#threading.thread --> thread constructor
			#args=client_scoket --> pass client socket to requesthandler as clientsocket
			threading.Thread(target=requestHandler, args=(client_socket,)).start()
	except:
		print("Exception caught")
		s.close()
#invoke main
main()
