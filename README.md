![GitHub](https://img.shields.io/github/license/mosiausi/psclap) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/mosiausi/psclap) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django) ![GitHub pull requests](https://img.shields.io/github/issues-pr/mosiausi/psclap) ![GitHub issues](https://img.shields.io/github/issues/mosiausi/psclap) 

For any question or suggestion, feel free to contact me: [![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/moshikon/)
&nbsp;

# Prob Sampler Closed Loop Automation Controller (psclap)
---------------------------------------------------------
Use case: poweroff MacOS/Linux-GNU devices which are not in use for 30 minutes based on active network sessions
Reason: I found that my NAS (which used for streaming only) mostly unused. 
Although the manufacturer claims for standby feature - this never really works!
I wanted a simply program on external device which will be able to turn off inactive device

# Presequences
    - Python3.7+ with paramiko
    - Prob to install this program. in my case Raspberry Pi Zero W

# Roadmap
    Q32020
        - Configurator for device parameters (hostname, username and password)
        - Encrypted password
    Q42020
        - Power on feature for local / remote(presequences TBC)

# Installation:
1. From your local machine, download the program: 

    ```git clone https://github.com/mosiausi/psclap```
2. At ```sessiondb.txt``` file, change the hostname/username/password for your desired environment

    note: do not change the order of ```sessiondb.txt```
3. add to your crontab:

    ```*/30 10-19 * * * python3 /path/scripts/sladpi.py > /path/psclap.log 2>&1```
