#!/usr/bin/python3
"""this is a program to get status"""
import urllib.request
import urllib.parse
import sys


obj = urllib.request.Request(sys.argv[1],method='GET')
with urllib.request.urlopen(obj) as response:
    print(response.headers())
