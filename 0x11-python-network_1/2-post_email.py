#!/usr/bin/python3
"""this is a program to get status"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': sys.argv[2]})
    email = email.encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], email) as response:
        print(response.decode('utf-8'))
