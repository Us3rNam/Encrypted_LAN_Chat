#!/usr/bin/env python

"""
Created By _UserName_

Uses an advanced form of the Ceasar Cipher
"""

class Crypt():
    def __init__(self):
        pass
    def __call__(self):
        return self
    
    
    def formatKey(self, origin_key, length):
        key = ""
        for i in range(len(origin_key)):
            key += str(ord(origin_key[i]))
        
        keyLength = len(key)
        block = 0
        
        if(keyLength == length):
            return key
        if(keyLength > length):
            return key[:length]
        if(keyLength < length):
            difference = length - keyLength
            for i in range(difference):
                key += key[(i - (keyLength * block))]
            return key
    
    def Encrypt(self, message, key):
        # Generate Key With Correct Length
        key = self.formatKey(key, len(message))
        # Encrypted Result
        encrypted = ""
        
        for i in range(len(message)):
            encrypted += str(chr( ord(message[i]) + int(key[i]) ))
        return encrypted
    
    def Decrypt(self, message, key):
        # Generate Key With Correct Length
        key = self.formatKey(key, len(message))
        # Decrypted Result
        decrypted = ""
        
        for i in range(len(message)):
            decrypted += str(chr( ord(message[i]) - int(key[i]) ))
        return decrypted
