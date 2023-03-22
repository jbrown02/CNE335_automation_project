# Joshua Brown
# 3/21/23
# CNE 335 Winter - Final Project

from Server import Server

def print_program_info():
    print("Server Automator v0.1 by Josh Brown")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    my_server_ip = "34.218.246.240"
    my_rsa_key_file = r"/Users/joshuabrown/attempt2.pem"
    username = "ec2-user"
    my_upgrade_command = "sudo yum update"
    my_server = Server(my_server_ip, my_rsa_key_file, username, my_upgrade_command)
    print(my_server.ping())
    print("Updating server")
    ssh_result = my_server.upgrade()
    print(''.join(ssh_result))
