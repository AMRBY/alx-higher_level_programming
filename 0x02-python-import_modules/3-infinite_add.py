#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    somme = 0
    while i < len(argv):
        somme = somme + int(argv[i])
        i += 1
    print("{}".format(somme))
