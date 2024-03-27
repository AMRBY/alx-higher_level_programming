#!/bin/bash
#display body size in bytes
curl -sI "$1" | grep Content-Length | cut -d" " -f2
