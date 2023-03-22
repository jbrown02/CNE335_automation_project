# Joshua Brown
# 3/21/23 - Winter
# CNE 335 - Server Automation

import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_file, username, upgrade_command):
        self.server_ip = server_ip
        self.username = username
        self.command = upgrade_command
        self.key_file = key_file

    def ping(self):
        response = os.system("ping -c 5 " + self.server_ip)
        if response == 0:
            return True
        else:
            return False

    def upgrade(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        k = paramiko.RSAKey.from_private_key_file(self.key_file)

        # Make the connection to the server
        ssh.connect(hostname=self.server_ip, username=self.username, pkey=k)

        stdin, stdout, stderr = ssh.exec_command(self.command)

        for line in stdout.read().splitlines():
            print(line)

        ssh.close()
