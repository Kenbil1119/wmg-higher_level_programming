#!/usr/bin/env python3
def uppercase(str):
    uppercase = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            uppercase += chr(ord(c) - 32)
        else:
            uppercase += c
    print("{}".format(uppercase))
