#!/bin/bash
#display methods
#curl -s -X OPTIONS "$1" | grep "Allow" | cut -d" " -f2
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
