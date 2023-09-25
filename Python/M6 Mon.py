# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:01:28 2022

@author: willi
"""

cipher = {'A': 'Z', 'B': 'A', 'C': 'V',  'D': 'K',  'E': 'F',  'F': 'D',  'G': 'X',  'H': 'C',  'I': 'G',  'J': 'E',  'K': 'W',  'L': 'L',  'M': 'I',  'N': 'P', 'O': 'Y',  'P': 'H', 'Q': 'R', 'R': 'B',  'S': 'N',  'T': 'S',  'U': 'J',  'V': 'M',  'W': 'O',  'X': 'Q',  'Y': 'U',  'Z': 'T'}
out = ''
words = 'The quick brown fox jumped over the lazy dog'

def encrypt(message, cipher):
    s =''
    message = message.upper()
    for char in message:
        if char not in cipher:
            s += char
            continue
        s += cipher[char]
    return s.upper()

def decrypt(message, cipher):
    s = ''
    message = message.upper()
    for char in message:
        for key in cipher:
            if cipher[key] == char:
                s += key
            elif char not in cipher:
                s += char
                break
    return s.lower()

if __name__ == "__main__":
    print(encrypt(words, cipher))
    print(decrypt(encrypt(words, cipher), cipher))
    print(decrypt('XZSFOZU VYIHJSGPX HUSCYP GN BFZLLU DJP!', cipher))