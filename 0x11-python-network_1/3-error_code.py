#!/usr/bin/python3
"""this is a program to get status"""
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    try:
        urllib.request.urlopen(sys.argv[1])
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
