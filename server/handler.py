"""
file: handler.py
language: python3
author: Rafid, Hans, Adam
description: This code handles http requests
"""
from httpparser import *
import subprocess
import httpresponse
import os

class Handler():

    def __init__(self, req):
        """
        Create handler object
        """

def serve_static(resource):
        res = httpresponse.ok()
        res = get_static_page(res, resource)
        return res


def serve_script(resource):
        file_name = resource
        if resource == "/":
            file_name="/index.php"

        try:
            path = "../php"+file_name
            if os.path.isfile(path):
                read_php = open(path , "r")
                page = subprocess.check_output("php-cgi -q " +  path,shell=True)
                res = httpresponse.ok()
                res.set_body(page.decode())
            else:
                res = httpresponse.notfound()
                res = get_static_page(res, "/not_found.html")
        except:
                res = httpresponse.internal_server_error()
                res = get_static_page(res, "/server_error.html")
        return res

def handle_client(connection , recvd_req , config):
        http_obj = HttpParser(connection , recvd_req , config)

        disabled_methods = config.get('SERVER','DISABLED_METHODS').split(',')

        req_method = http_obj.get_method()
        if req_method in disabled_methods:
            res = httpresponse.methodnotallowed()

        elif req_method == "GET":
            resource = http_obj.get_uri()

            if resource == "/" or resource.split(".")[-1] == "php":
                res = serve_script(resource)
            elif resource.split(".")[-1] == "css" or resource.split(".")[-1] == "js" or resource.split(".")[-1] == "html":
                res = serve_static(resource)
            else:
                res = httpresponse.notfound()
                res = get_static_page(res, "/not_found.html")

        elif req_method == "POST":
            resource = http_obj.get_uri()
            print("[*] POST REQUEST : ",resource)
            if resource == "/" or resource.split(".")[-1] == "php":
                res = serve_script(resource)
            elif resource.split(".")[-1] == "css" or resource.split(".")[-1] == "js" or resource.split(".")[-1] == "html":
                res = serve_static(resource)
            else:
                res = httpresponse.notfound()
                res = get_static_page(res, "/not_found.html")

        connection.send(res.send().encode())  # send data to socket
        connection.close()


def get_static_page(res, path):
    mfile = open("../php"+path)
    res.set_body(mfile.read())
    return res

if __name__ == '__main__':
    req =     req = b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nUser-Agent: curl/7.55.1\r\nAccept: application/json\r\n\r\n'
    handle_client(None, req, None)
