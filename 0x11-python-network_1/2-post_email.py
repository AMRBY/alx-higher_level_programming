#!/usr/bin/python3
"""this is a program to get status"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        print(response.decode('utf-8'))
