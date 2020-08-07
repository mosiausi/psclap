![GitHub](https://img.shields.io/github/license/mosiausi/psclap) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/mosiausi/psclap) ![GitHub Release Date](https://img.shields.io/github/release-date/mosiausi/psclap) <br> ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django)
![GitHub repo size](https://img.shields.io/github/repo-size/mosiausi/psclap) ![GitHub pull requests](https://img.shields.io/github/issues-pr/mosiausi/psclap) ![GitHub All Releases](https://img.shields.io/github/downloads/mosiausi/psclap/total) ![GitHub issues](https://img.shields.io/github/issues/mosiausi/psclap) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/mosiausi/psclap) ![GitHub last commit](https://img.shields.io/github/last-commit/mosiausi/psclap)

Please feel free to contact me: [![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/moshikon/)
&nbsp;

# Prob Sampler Closed Loop Automation Controller (psclap)
---------------------------------------------------------
Use case: poweroff MacOS/Linux-GNU/Unix devices which are not in use for 30 minutes based on active network sessions
Reason: I wanted my NAS to turn off when it's not in use for some period of time. 
Although the manufacturers claims for standby feature - this never really works!
I wanted a simpl program on external device which will be able to turn off an inactive device

# Presequences
    - Python3.7+ with paramiko
    - Prob to install this program. in my case Raspberry Pi Zero W

# Roadmap
    Q32020
        - Encrypted password
    Q42020
        - Costume scheduler 

# Installation:
1. From your local machine, download or clone the program: 

    ```git clone https://github.com/mosiausi/psclap```
2. Enter to the psclap directory and run the setup (crucial)

    ```cd /[path of psclap]```
3. run the setup.py from the local directory of psclap

    ```python3 setup.py```
3. add to your crontab:

    ```*/30 10-19 * * * python3 /path/scripts/sladpi.py > /path/psclap.log 2>&1```
4. add to your crontab:

I hope this little program will serve you well.

# Release notes:

1R1.2 7/8/2020<BR>
    setup.py: Adding an install procedure for this program.

1R1.1 - 5/8/2020
    Initial Release
