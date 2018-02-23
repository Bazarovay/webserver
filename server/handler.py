"""
file: handler.py
language: python3
author: Rafid, Hans, Adam
description: This code handles http requests
"""
from httpparser import *
from httprequest import *
import subprocess
import httpresponse
import os
import socket

class Handler():

    def __init__(self, req):
        """
        Create handler object
        """

def serve_static(resource):
        res = httpresponse.ok()
        res = get_static_page(res, resource)
        return res


def serve_script(req, resource):
        file_name = resource
        if resource == "/":
            file_name="/index.php"

        try:

            path = "/var/www/html/webserver/php"+file_name
            print(path)
            if os.path.isfile(path):
                # print(path)
                command = "export REQUEST_METHOD='%s'; " %(req.get_method())
                command += "export QUERY_STRING='%s'; " %(str(req.get_params()))
                command += "export SCRIPT_FILENAME='%s'; " % (path)
                command += " sudo php-cgi -f '%s'" % (path)

                page = subprocess.check_output(command,shell=True)
                res = httpresponse.ok()
                res.set_body(page.decode())
            else:
                res = httpresponse.notfound()
                res = get_static_page(res, "/not_found.html")
        except Exception as e:
                print(e)
                res = httpresponse.internal_server_error()
                res = get_static_page(res, "/server_error.html")
        return res

def handle_client(connection , recvd_req , config):
        http_obj = HttpParser(connection , recvd_req , config)

        disabled_methods = config.get('SERVER','DISABLED_METHODS').split(',')

        req_method = http_obj.get_method()
        print("--------------")
        print(req_method)
        doc_root = "/var/www/html/webserver/php"
        resource = http_obj.get_resource()
        if req_method in disabled_methods:

            res = httpresponse.methodnotallowed()
        # elif req_method == "PUT":



        elif req_method == "HEAD":
            res = httpresponse.ok()
            res.set_header("HOST","localhost:8080")
            res.set_body("Head request made")
        elif req_method == "CONNECT":
            res = HttpRequest(method="GET",uri="www.facebook.com");
            sending = res.send()
            print(sending)
            print(repr(sending))
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            addr = ('www.facebook.com',80)
            ss.connect(addr)
            ss.send(sending.encode())
            resp = ss.recv(1000)
            ss.close()
            print(resp)
            res = httpresponse.ok()
            res.set_header("HOST","localhost:8080")
            res.set_body(str(resp))
        elif req_method == "PUT":
            print("***************************8PUT")
            with open(doc_root+resource,'w') as myFile:
                response = "HTTP/1.1 200 OK\r\n"
                myFile.write(str(http_obj))

            res = httpresponse.ok()
            res.set_header("HOST","localhost:8080")
            res.set_body("PUT request made")

        elif req_method == "DELETE":
            response = "HTTP/1.1 200 OK\r\n"
            os.remove(doc_root+resource)
            res = httpresponse.ok()
            res.set_header("HOST","localhost:8080")
            res.set_body("DELETE request made")

        elif req_method == "GET":
            resource = http_obj.get_resource()
            print("*******************************************8")
            print(resource)

            if resource == "/" or resource.split(".")[-1] == "php":
                if resource == "/400.php":
                    res = httpresponse.unauthorized()
                elif resource == "/401.php":
                    res = httpresponse.bad_request()
                elif resource == "/402.php":
                    res = httpresponse.payment_required()
                elif resource == "/403.php":
                    res = httpresponse.forbidden()
                elif resource == "/411.php":
                    res = httpresponse.lenreqd()
                elif resource == "/505.php":
                    res = httpresponse.version_not_supported()
                else:
                    res = serve_script(http_obj, resource)
            elif resource.split(".")[-1] == "css" or resource.split(".")[-1] == "js" or resource.split(".")[-1] == "html":
                res = serve_static(resource)
            else:
                res = httpresponse.notfound()
                res = get_static_page(res, "/not_found.html")

        elif req_method == "POST":
            resource = http_obj.get_uri()
            print("[*] POST REQUEST : ",resource)
            print("******************")
            print(http_obj.get_body())
            # php -B "\$_POST = array('username' => 'val1', 'password' => 'val2');" -F checklogin.php
            # php -B "\$_POST = array('username' => 'val1', 'password' => 'val2');" -F checklogin.php

            if resource == "/" or resource.split(".")[-1] == "php":
                try:
                    command = " export REQUEST_METHOD=POST;"
                    command += " export SCRIPT_FILENAME='%s%s';" %('/var/www/html/webserver/php',resource)
                    command += " export CONTENT_LENGTH=%s;"%(str(len(str(http_obj.body))))
                    command += "export REDIRECT_STATUS=true;"
                    command += "export CONTENT_TYPE='application/x-www-form-urlencoded'; "
                    command += " export BODY=\"%s\";"%(str(http_obj.body))
                    command += "exec echo $BODY"
                    command += " | php-cgi -q"
                    page = subprocess.getoutput(command)
                    res = httpresponse.ok()
                    res.set_body(page)
                except subprocess.CalledProcessError as e:
                    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
                    res = httpresponse.ok()
                    res.set_body(page.decode())
                # except Exception as e:
                    # print(e)

                # res = serve_script(resource)
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
