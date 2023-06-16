# https://www.lintcode.com/problem/659/description
"""
Design an algorithm to encode a list of strings to a string.
The encoded string is sent over the network and is decoded back to the original list of string. Implement 'encode' and 'decode'

# input:  ['lint', 'code', 'love', 'you']
# output: ['lint', 'code', 'love', 'you'] // one possible encode method is: 'lint:;code:;love:;you'
------------------------------------------------------------------------------------------------
def encode(strs):           Incredibly naive approach (using delimiter char)
    return '#'.join(strs)

def decode(str):            The problem is that any delimiter char can appear in any word, making it impossible to differenciate
    return str.split('#')   if it is the actual delimiter, or a char part of any word
----------------------------------------------------------------------------------------------------
"""

# strategy is to encode the string: <wordLength>#<word>
#                                               ^ (some delimiter char)
# if we always know the length of the word, it doesn't matter if the delimiter char appears in the word. We know where it starts
def encode(strings):
    encoded = []
    for word in strings:
        encoded.append(str(len(word)))  # append length of the word (consider it could be one, two, three chars...)
        encoded.append('#')             # then delimiter
        encoded.append(word)            # then actual word

    return ''.join(encoded)

def decode(string):
    decoded = []
    i = 0                              # i is index to traverse the encoded string, from the beginning
    
    while i < len(string):
        j = i                          # j starts at i
        while string[j] != '#':        # collect the numerical portion that represents the word length
            j += 1                     # increase j, until finding the char '#'
        
                                               # at this point, j is pointing at char '#'
        length = int(string[i:(j)])            # length is at substring [i:j] (last index is not inclusive! so last index: j-1)
        word = string[(j+1): (j + 1 + length)] # word is substring: [(one after j) : (next to j + length)] (last not inclusive)
        decoded.append(word)                   # append the word to the result array
        i = j + 1 + length                     # move i to position (next to j + length), so the index not included in substring

    return decoded
    

# O(n) TIME where n is the total number of chars among all words // encode: O(n) + decode O(n) = O(2n) -> O(n)
# O(n) space

encoded = encode(['lint', 'code', 'love', 'you'])
print(encoded)

decoded = decode(encoded)
print(decoded)

