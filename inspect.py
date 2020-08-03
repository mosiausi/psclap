#!/usr/bin/env python3
import subprocess
import platform

current_ip_address = ['192.168.0.37']
#test

def ping_ip(current_ip_address):
    try:
        output = subprocess.check_output("ping -{} 1 {} -i 0.2 -s 1 -W 1".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            return False
        else:
            return True
    except (ValueError, Exception):
        return False


if __name__ == '__main__':
    for each in current_ip_address:
        if ping_ip(each):
            print(each, "is available.\n")
            import deepinspection
        else:
            print(each, "is not available.")
