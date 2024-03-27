#!/bin/bash
#display body
x=$(curl -X GET -si "$1" | grep "200")
if [ -n "$x" ]
then
	curl "$1"
fi
