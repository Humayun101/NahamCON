#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 22:34:09 2025

@author: humayun404
"""

def vigenere_decrypt(ciphertext, key):
    result = []
    j = 0
    key = key.lower()
    
    for c in ciphertext:
        if c.isalpha():
            is_upper = c.isupper()
            c_val = ord(c.lower()) - ord('a')
            k_val = ord(key[j % len(key)]) - ord('a')
            p_val = (c_val - k_val + 26) % 26
            p_char = chr(p_val + ord('a'))
            result.append(p_char.upper() if is_upper else p_char)
            j += 1
        else:
            result.append(c)
    
    return ''.join(result)

ciphertext = "YeaTtgUnzezBqiwa2025"
key = "nahamcon"

password = vigenere_decrypt(ciphertext, key)
print("Decrypted password:", password)
