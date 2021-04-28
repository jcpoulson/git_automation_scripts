import subprocess

subprocess.call(["ssh", "-p", "2220", "bandit0@bandit.labs.overthewire.org"])
subprocess.call(["bandit0"])