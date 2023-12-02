#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    x = dir(hidden_4)
    lenght = len(dir(hidden_4))
    i = 0
    while i < lenght:
        if x[i][0] != "_":
            print("{}".format(x[i]))
        i += 1
