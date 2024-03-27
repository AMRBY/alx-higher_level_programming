#!/bin/bash
#display methods
curl -sX OPTIONS "$1" | grep "Allow" | cut -d" " -f2
