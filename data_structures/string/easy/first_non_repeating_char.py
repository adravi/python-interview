# https://www.algoexpert.io/questions/first-non-repeating-character
# input: string = 'abcdcaf'
# output: 1 // the first non-repeating char is 'b', found at index 1

def firstNonRepeatingChar(string):
    nonRepDict = {}

    for char in string:
        if char not in nonRepDict:
            nonRepDict[char] = 1
        else:
            nonRepDict[char] += 1

    for i,char in enumerate(string):
        if nonRepDict[char] > 1:
            continue
        else:
            return i
        
    return -1

# O(2n) -> O(n) time
# O(26) -> O(1) space  // We know there's a fixed number of letters in the english alphabet, so it's constant aux mem

# -------------------------------------------------------------------
def firstNonRepeatingChar2(string):
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
