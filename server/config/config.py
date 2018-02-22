# """
# """
# import configparser
# import sys
#
# class Config():
#
#     __slots__ = ["permitted","bind_ip","bind_port","script"]
#     def __init__(self):
#
#         if (len(sys.argv) < 2):
#             print("***\nNo configuration file was added. Will load default configuration.\n***")
#             conf_path = "config/default.cnf"
#         else:
#             conf_path = sys.argv[1]
#
#         print("---------")
#         print(conf_path)
#         print("----------")
#         config = configparser.ConfigParser()
#         config.read(conf_path)
#         self.bind_ip = config.get('SERVER' , 'IP')
#         self.bind_port = int(config.get('SERVER', 'PORT'))
#         self.permitted = config.get('SERVER','PERMITTED_METHODS').split(',')
#         self.script = config.get('SERVER','SCRIPT')
#
# # [-] Uses a configuration file for the following server settings:
# #   [] Permit disabling any of the above HTTP methods
# #   [] Root folder for the web application on the host
# #
# # [] Uses one or more configuration files for specifying what server-side scripting languages are supported and/or how to execute them
#
#
# Config()
