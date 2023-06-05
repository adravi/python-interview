# https://www.algoexpert.io/questions/first-non-repeating-character
# input: string = 'abcdcaf'
# output: 1 // the first non-repeating char is 'b', found at index 1

def firstNonRepeatingChar(string):
    charSet = set()
    nonRepMap = {}

    for i, char in enumerate(string):
        if char not in charSet:
            charSet.add(char)
            nonRepMap[char] = i
        else:
            nonRepMap.pop(char, None)

    if len(nonRepMap) == 0:
        return -1
    else:
        minKey = min(nonRepMap, key=nonRepMap.get)
        return nonRepMap[minKey]
            

print(firstNonRepeatingChar("ggyllaylacrhdzedddjsc"))
