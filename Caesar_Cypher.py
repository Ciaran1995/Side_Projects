#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:22:29 2021

@author: ciaranmcdonnell
"""

"""
Basic Caeser Cypher:
    1) Need the message to encrypt - each character accessible individually.
    2) Need the encryption key
    3) Need to move each character the key amount modulo the length of the string.
"""
import string as st

alphabet_list = list(st.ascii_lowercase)
alphabet_list.append(' ')

def encrypt(msg, ky):
    message_encrypted = []
    message_list = list(msg)
    for i in range(len(msg)):
        indx = alphabet_list.index(message_list[i])
        message_encrypted.append(alphabet_list[(indx + int(ky))%(len(alphabet_list))])
    return ''.join(message_encrypted)

def decrypt(msg,ky):
    message_decrypted = []
    message_list = list(msg)
    for i in range(len(msg)):
        indx = alphabet_list.index(message_list[i])
        message_decrypted.append(alphabet_list[(indx - int(ky))%(len(alphabet_list))])
    return ''.join(message_decrypted)

print('=========== Caesar Cypher ===========\n')
message = input("Type in your message to be encrypted now: ").lower()
key = input("What key would you like to use to encrypt your message?: ")

encryption = encrypt(message, key)     

print('Your encrypted message is: ' + encryption)

undo = input('\nWould you like to decrypt your message? y/n : ')
if undo == 'y':
    print('The encrypted message was: ' + decrypt(encryption,key))
else:
    print("Alright then, keep your secrets!")    


# message_encrypted = []
# message_list = list(message)
# for i in range(len(message)):
#     indx = alphabet_list.index(message_list[i])
#     print(indx+int(key))
#     message_encrypted.append(alphabet_list[(indx + int(key))%(len(st.ascii_lowercase)-1)])