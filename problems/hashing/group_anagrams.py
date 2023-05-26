# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    map = {}
    for word in strs:
        # Sort the word alphabetically -> O(log(n))
        sorted_word="".join(sorted(word))
        
        # The sortedWord does not exist in map
        if sorted_word not in map:
            map[sorted_word] = [word]
        else:
            map[sorted_word].append(word)

    return map.values()

# O(n log(n)) Time
# O(n) Space

            