"""
file: handler.py
language: python3
author: Rafid, Hans, Adam
description: This code handles http requests
"""
from httpparser import *
import subprocess
import httpresponse

class Handler():

    def __init__(self, req):
        """
        Create handler object
        """




def handle_client(connection , recvd_req , config):
        http_obj = HttpParser(connection , recvd_req , config)
        # print(http_obj)

        if http_obj.get_method() == "GET":
            resource = http_obj.get_uri()
            if resource == "/":
                file_name="/index.php"

            # print()
            read_php = open("../php/index.php" , "r")
            page = subprocess.check_output("php-cgi -q " +  "../php/index.php",shell=True)
            res = httpresponse.ok()
            print("------------------------------")
            print(page)
            print("------------------------------")
            res.set_body(page.decode())
            print(res.send())
            connection.send(res.send().encode())  # send data to socket
            connection.close()
	    # try:    #if it is, open it and send it to client
		# open(process_request[0][1][1:])
		# x=subprocess.check_output("php-cgi " + process_request[0][1][1:] ,shell=True)
		# http_response = http_response + x
        #
	    # except:  # if no such file, respond with 404
		# http_response = http_response + "HTTP/1.1 404p Not Found\r\n\r\n"
        # print "Replying with %s" % http_response

if __name__ == '__main__':
    req =     req = b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.55.1\r\nAccept: application/json\r\n\r\n'
    handle_client(None, req, None)
