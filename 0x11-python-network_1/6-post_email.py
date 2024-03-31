#!/usr/bin/python3
"""this is a program to get status"""
import sys
import requests

if __name__ == "__main__":
    email = sys.argv[2]
    req = requests.post(sys.argv[1], data={'email': email})
    print(req.text)
