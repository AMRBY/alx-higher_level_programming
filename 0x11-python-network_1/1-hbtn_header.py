#!/usr/bin/python3
"""this is a program to get status"""
import urllib.request
import sys


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.method('GET')
    print(f"\t- content: {html}")
