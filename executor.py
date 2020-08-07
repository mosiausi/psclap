#!/usr/bin/env python3
from typing import List

import paramiko

commands = [
    "netstat -tun | grep -v '127.0.0.1' | awk '{print $6}' |"
    " sort | uniq -c | sort -n | grep ESTABLISHED | awk '{print $1}'"
]
actions = "poweroff"
file = open("sessionsdb.txt")
sessionsdb: List[str] = file.read().splitlines()

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=sessionsdb[0], username=sessionsdb[1], password=sessionsdb[2])
except Exception as e:
    print(e, "[!]")
    exit()
# execute the commands
for command in commands:
    # print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    conn = int(stdout.read().decode())
    concurrent = int(sessionsdb[3])
    if conn <= concurrent:
        print("Less than ({})".format(conn), "connections."
              " Deploy: <{}>".format(actions), "command using SSH."),
        stdin, stdout, stderr = client.exec_command(actions)
        print(stdout.read().decode())
    elif conn > concurrent:
        print("More than ({})".format(conn), "connections."
              " This program will be terminated")
# Clean up elements
client.close()
del client, stdin, stdout, stderr
