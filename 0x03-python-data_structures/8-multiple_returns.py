#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent > 0:
        sen = sentence[0]
    else:
        sen = None
    return (lent, sen)
