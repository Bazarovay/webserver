import socket 
import subprocess

HOST, PORT = '0.0.0.0', 8888 #set host and port

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set socket to IPV4 and connect to TCP
listen_socket.bind((HOST, PORT)) # bind the socket to the address
listen_socket.listen(5) # maximum number of connections
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()  # connect client to server
    request = client_connection.recv(1024)  #receive data from socket, max data size 1024
    requestline = request.split('\n') # split request by "\n"
    process_request=[]
    process_request.append(requestline[0].strip().split(' ')) # show results split by space
    for line in requestline[1:]:  #for loop to show only the host line
	if line[0:4] == "Host":
		#handle host case
		header = "Host"
		rest = line[6:].strip()
		hostline = []
		hostline.append(header)
		hostline.append(rest)
		process_request.append(hostline)
		
		
	else:
		#handle all other cases
		process_request.append(line.strip().split(':'))
    print process_request[0][1][1:]  # print out the file name
    http_response=""
    if process_request[0][1][1:][-5:] == ".html":    #check if the file is HTML file,
	    try:   # if it is, open the file and response to the client.
		http_response = http_response + "HTTP/1.1 200 OK\r\n\r\n"
	    	file = open(process_request[0][1][1:])  #open file by name
		filetext=''
	    	for fileline in file:    #for loop to print out file
			filetext+=fileline
		http_response = http_response + filetext
	   	print "Responding with %s" % http_response
	    except:    # if there is no such file, respond with 404.
		#respond with error code
		http_response = http_response + "HTTP/1.1 404 Not Found\r\n\r\n"

    elif process_request[0][1][1:][-4:] == ".php":    # check if the file is php file.
	    try:    #if it is, open it and send it to client
		open(process_request[0][1][1:])
		x=subprocess.check_output("php-cgi " + process_request[0][1][1:] ,shell=True)
		http_response = http_response + x

	    except:  # if no such file, respond with 404
		http_response = http_response + "HTTP/1.1 404p Not Found\r\n\r\n"		
		print "Replying with %s" % http_response

    elif process_request[0][1][1:][-4:] == ".css":    #  if the HTML contains css file, check if it exists.
	    try:	#if it exists, open it and send it. 
		file = open(process_request[0][1][1:])
		csstext=''
		for fileline in file:
			csstext+=fileline

		http_response = http_response + csstext

		
	    except:    # if it's not there, send 404.
		http_response = http_response + "HTTP/1.1 404p Not Found\r\n\r\n"		
		print "Replying with %s" % http_response    


    else:      # all other files, send 404 to client.
	
        http_response = http_response + "HTTP/1.1 404 Not Found\r\n\r\n"
	

    client_connection.send(http_response)  # send data to socket
    client_connection.close()    # close the socket
   



