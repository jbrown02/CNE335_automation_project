# Joshua Brown
# 3/7/23 - Winter
# CNE 335 - Server Automation

import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        response = os.system("ping -c 1 " + self)
        if response == 0:
            return True
        else:
            return False
