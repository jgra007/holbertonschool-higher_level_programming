#!/usr/bin/python3


def remove_char_at(str, n):
    if n < 0:
        return str
    if n > len(str):
        return str
    newstr = ""
    if len(str) > n:
        newstr = str[0:n] + str[n+1:]
    return newstr
