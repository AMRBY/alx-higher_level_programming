#!/bin/bash
#display methods
curl -sI "$1" | grep "Allow:" | cut -d" " -f2
