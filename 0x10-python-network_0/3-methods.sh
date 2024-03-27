#!/bin/bash
#display methods
curl -s -X OPTIONS "$1" | grep "Allow" | cut -d" " -f2
