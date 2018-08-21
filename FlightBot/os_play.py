import spur
import spur.ssh


shell = spur.SshShell(hostname="10.14.194.150", username="ubuntu", password="autonomous", missing_host_key=spur.ssh.MissingHostKey.accept)
with shell:
    result = shell.run(["echo", "hello"])
print(result.output)

#result = shell.run(["echo", "-n", "hello"])
#print result.output # prints hello
'''

#more solutions

import os

ssh = paramiko.SSHClient()
ssh.connect(server, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)

import os
import sys
import select
import paramiko
import time


class Commands:
    def __init__(self, retry_time=0):
        self.retry_time = retry_time
        pass

    def run_cmd(self, host_ip, cmd_list):
        i = 0
        while True:
        # print("Trying to connect to %s (%i/%i)" % (self.host, i, self.retry_time))
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host_ip)
            break
        except paramiko.AuthenticationException:
            print("Authentication failed when connecting to %s" % host_ip)
            sys.exit(1)
        except:
            print("Could not SSH to %s, waiting for it to start" % host_ip)
            i += 1
            time.sleep(2)

        # If we could not connect within time limit
        if i >= self.retry_time:
            print("Could not connect to %s. Giving up" % host_ip)
            sys.exit(1)
        # After connection is successful
        # Send the command
        for command in cmd_list:
            # print command
            print "> " + command
            # execute commands
            stdin, stdout, stderr = ssh.exec_command(command)
            # TODO() : if an error is thrown, stop further rules and revert back changes
            # Wait for the command to terminate
            while not stdout.channel.exit_status_ready():
                # Only print data if there is data to read in the channel
                if stdout.channel.recv_ready():
                    rl, wl, xl = select.select([ stdout.channel ], [ ], [ ], 0.0)
                    if len(rl) > 0:
                        tmp = stdout.channel.recv(1024)
                        output = tmp.decode()
                        print output

        # Close SSH connection
        ssh.close()
        return

def main(args=None):
    if args is None:
        print "arguments expected"
    else:
        # args = {'<ip_address>', <list_of_commands>}
        mytest = Commands()
        mytest.run_cmd(host_ip=args[0], cmd_list=args[1])
    return


if __name__ == "__main__":
    main(sys.argv[1:])
'''
