#!/bin/bash
#display body size in bytes
x=$(curl -si "$1" | grep "200")
if [ ! -z $x ]
then
	curl "$1"
fi
