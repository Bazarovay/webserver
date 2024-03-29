"""
file: main.py
language: python3
author: Rafid, Hans, Adam
description: This is the main file and sets up a python server. Incoming requests
are received here and forwarded to handlers
"""
import socket
import configparser
import sys
import threading
from handler import *
import ruby_handler

def read_config():
    """
    Reads configuration file for server address and port.
    Reads default path if none added
    :params None
    :return configuration (configparser object)
    """
    if (len(sys.argv) < 2):
        print("***\nNo configuration file was added. Will load default configuration.\n***")
        conf_path = "config/default.cnf"
    else:
        conf_path = sys.argv[1]

    config = configparser.ConfigParser()
    config.read(conf_path)
    return config

def create_socket(config):
    """
    Start listening on confiured port and return socket
    params: config (configparser)
    returns: socket (Socket)
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ERRNO 98
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    bind_ip = config.get('SERVER' , 'IP')
    bind_port = int(config.get('SERVER', 'PORT'))
    sock.bind((bind_ip, bind_port))
    sock.listen(1)

    print("[*] Listening on %s:%s | 5 connections" % (bind_ip,bind_port))
    return sock

def read_requests(socket, config):
    """
    Read incoming requests and pass on to handler thread
    params: socket
    returns: None
    """
    while True:
        client, address = socket.accept()
        print("[*] Connection accepted from %s:%d" %(address[0],address[1]))
        recvd_req = client.recv(2048)
        print(recvd_req)
        if int(config.get('SERVER','PORT')) == 8081:
            print("RUBY SERVE")
            client_handler = threading.Thread(target=ruby_handler.handle_client, args=(client,recvd_req,config))
        else:
            client_handler = threading.Thread(target=handle_client, args=(client,recvd_req,config))
        client_handler.start()

def main():
    """
    reads config, creates server and then reads incoming requests
    params: None
    returns: None
    """
    config = read_config()
    sock = create_socket(config)
    read_requests(sock, config)

if __name__ == "__main__":
    main()
