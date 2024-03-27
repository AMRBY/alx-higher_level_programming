#!/usr/bin/env bash
#display body size in bytes
curl -sI ubuntu@35.175.129.122 | grep Content-Length | cut -d" " -f2
