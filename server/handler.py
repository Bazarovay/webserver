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
        print(http_obj)

        if http_obj.get_method() == "GET":
            resource = http_obj.get_uri()
            print("-------------------------")
            print(resource)
            print("-------------------------")
            if resource == "/" or resource.split(".")[-1] == "php":
                print(resource)
                file_name = resource
                if resource == "/":
                    file_name="/index.php"

                path = "../php"+file_name
                print(path)
                read_php = open(path , "r")
                page = subprocess.check_output("php-cgi -q " +  path,shell=True)
                res = httpresponse.ok()
                res.set_body(page.decode())

            if resource.split(".")[-1] == "css" or resource.split(".")[-1] == "js" or resource.split(".")[-1] == "html":
                print(resource)
                mfile = open("../php"+resource)
                csstext=''
                for fileline in mfile:
                    csstext+=fileline

                res = httpresponse.ok()
                res.set_body(csstext)

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
