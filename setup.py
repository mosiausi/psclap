#!/usr/bin/env python3

print("initiate psclap installation process. Please configure your target compute device.""\n")
text_file = open("sessionsdb.txt", "w")

value_list = []


for i in range(1):
    print("IP address or hostname: ")
    line = input()
    value_list.append(line + "\n")
    print("Username: ")
    line = input()
    value_list.append(line + "\n")
    print("Password: ")
    line = input()
    value_list.append(line + "\n")
    print("Set the minimum amount of active connections to keep the target compute node alive: ")
    line = input()
    value_list.append(line + "\n")


text_file.writelines(value_list)

text_file.close()

print("Configuration has been successfully completed.""\n"
      "Please add a cron job to run sladpi.py with root permissions")
print("You can re-install to modify the configuration")
