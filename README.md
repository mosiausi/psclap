![](https://img.shields.io/badge/build-development-orange) ![](https://img.shields.io/badge/python-3.7|3.8-blue) ![](https://img.shields.io/badge/license-nayman-yellowgreen)

# Prob Sampler Closed Loop Automation Controller (psclap)

Use case: poweroff MacOS/Linux-GNU devices which are not in use for 30 minutes based on active network sessions
Reason: I found that my NAS (which used for streaming only) mostly unused. 
Although the manufacturer claims for standby feature - this never really works!
I wanted a simply program on external device which will be able to turn off inactive device

Installation:
1. From your local machine, download the program: 

    ```git clone https://github.com/mosiausi/psclap```


2. At ```sessiondb.txt``` file, change the hostname/username/password for your desired environment

note: do not change the order of ```sessiondb.txt```


3. add to your crontab:

    ```*/30 10-19 * * * python3 /path/scripts/sladpi.py > /path/psclap.log 2>&1```
