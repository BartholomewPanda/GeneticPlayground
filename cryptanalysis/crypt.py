#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import sys


def crypt(key, msg):
    cipher = []
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            pos_c = ord(c) - ord('a')
            pos_k = ord(key[i]) - ord('a')
            cipher.append(chr((pos_c + pos_k) % 26 + ord('a')))
            i = (i + 1) % len(key)
        else:
            cipher.append(c)
    return ''.join(cipher)

def decrypt(key, msg):
    cipher = []
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            pos_c = ord(c) - ord('a')
            pos_k = ord(key[i]) - ord('a')
            cipher.append(chr((pos_c - pos_k) % 26 + ord('a')))
            i = (i + 1) % len(key)
        else:
            cipher.append(c)
    return ''.join(cipher)


if __name__ == '__main__':
    if len(sys.argv) != 4 or not sys.argv[1] in ['-e', '-d']:
        print('usage: %s -e|-d key file' % sys.argv[0])
        sys.exit(1)
    cmd = sys.argv[1]
    key = sys.argv[2]
    path = sys.argv[3]
    with open(path) as f:
        data = f.read()
    if cmd == '-e':
        print(crypt(key, data))
    else:
        print(decrypt(key, data))
