#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        x = ord(str[i])
        if x > 96 and x < 123:
            x -= 32
        print("{}".format(chr(x)), end='')
    print('')
