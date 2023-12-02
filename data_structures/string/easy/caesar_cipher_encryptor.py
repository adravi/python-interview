# https://www.algoexpert.io/questions/caesar-cipher-encryptor

# input: string = 'xyz', key = 2
# output: 'zab'

def caesar_cipher_ecryptor(string, key):
    newStringChars = []                     # ASCI values | 'a': 97, 'z': 122 | 26 chars from 'a' -to- 'z'

    for char in string:
        key = key % 26                      # for large keys, make sure to keep in the range: 0-26 (alphabet length)
        newCharVal = int(ord(char)) + key   # add up the key to the char value. Remember ord() returns a decimal!

        if newCharVal > 122:                       # In case the new value goes beyond 122 (the value of 'z')
            newCharVal = (newCharVal % 122) + 96   # Apply a function to keep it in the range: 97-122

        newStringChars.append(chr(newCharVal))

    return ''.join(newStringChars)

# O(n) time
# O(n) space


result = caesarCipherEncryptor('abc', 52)
print(result)