#!/usr/bin/python3
"""this is a program to get status"""
import urllib.request
import sys


with urllib.request.Request('https://alx-intranet.hbtn.io/status', 'GET') as response:
    html = response
    print(f"\t- content: {html}")
