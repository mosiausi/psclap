#!/usr/bin/env python3
from typing import List
import subprocess
import platform


def ping_ip(sessionsdb):
    try:
        file = open("sessionsdb.txt")
        sessionsdb: List[str] = file.read().splitlines()
        output = subprocess.check_output("ping -{} 1 {} -i 0.2 -s 1 -W 1".format('n' if platform.system().lower(
        ) == "windows" else 'c', sessionsdb[0]), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            return False
        else:
            return True
    except (ValueError, Exception):
        return False


file = open("sessionsdb.txt")
sessionsdb: [str] = file.read().splitlines()

if ping_ip(sessionsdb):
    print(sessionsdb[0], "is online.\n")
    import executor
else:
    print(sessionsdb[0], "is offline.")
