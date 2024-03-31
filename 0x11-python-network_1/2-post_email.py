#!/usr/bin/python3
"""this is a program to get status"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], email)

    with urllib.request.urlopen(req) as response:
        print(response.decode('utf-8'))
