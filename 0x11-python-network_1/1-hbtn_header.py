#!/usr/bin/python3
"""this is a program to get status"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    obj = urllib.request.Request(sys.argv[1], method='GET')
    with urllib.request.urlopen(obj) as response:
        print(response.headers.get('X-Request-Id'))
