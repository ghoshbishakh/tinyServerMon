#!/usr/bin/python3
import subprocess
import sys

def du(path):
    """disk usage in human readable format (e.g. '2,1GB')"""
    return subprocess.check_output(['du','-shx', path]).split()[0].decode('utf-8')

if __name__ == "__main__":
    path = sys.argv[1]
    print(du(path))