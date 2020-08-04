![](https://img.shields.io/badge/build-passing-brightgreen) ![](https://img.shields.io/badge/python-3.7|3.8-blue)


# PowerManagement
# This program devided into two Python script

# 1. mnping.py send a smal ICMP packet to check if the server is up, if not, the program will be terminated.
# 2. mnping will execute mnnetstat.py if server is up (pingable)
# 3. mnnetstat.py will connect with SSH to the server and check the number of established connections. if more than (x) it will be terminated
# - if less than (x), the program will execute poweroff
