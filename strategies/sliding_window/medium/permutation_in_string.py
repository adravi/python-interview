# https://leetcode.com/problems/permutation-in-string/
# given 2 strings, s1 (of size m) and s2 (of size n) that only contain lowercase english letters (26)
# return true if s2 contains a permutation of s1, or false otherwise (if one of s1's permutations is the substring of s2)

# input: s1 = "ab", s2 = "eidbaooo"
# output: true // s2 contains one permutation of s1 ("ba")

# to be true, a window (substring) of size m (s1) containing the same letters as in s1, MUST EXIST IN s2
# have 2 hashmaps {a:1, ..., z:1} storing the appearances of each letter given a window of size m / this works as a matches-state
# strategy will be: moving the window to the right, updatung the matches-state
def checkInclusion(s1, s2): 
    if len(s1) > len(s2):       # s1 needs to be smaller than s2
        return False

    map1, map2 = {}, {}
    for i in range(97, 123):    # build the hashmaps with keys being letters from a - z
        map1[chr(i)] = 0        # 'a': 97, 'z': 122 | O(26)
        map2[chr(i)] = 0
    
    for i in range(len(s1)):    # fill-up both hashmaps, cosidering the appearances of letters in s1 / this is the first window
        map1[s1[i]] += 1        # O(m)
        map2[s2[i]] += 1

    matches = 0
    for i in range(97, 123):    # starting from the first window 0 - (len(s1)-1) count the number of matches / no appearances count!
        if map1[chr(i)] == map2[chr(i)]:
            matches += 1

    left = 0                    # letter to remove from window (one to the left)
    right = len(s1)             # letter to add to window (one to the right)
    while right < len(s2):
        if matches == 26:       # if matches == 26, you are done
            return True
        
        letterAdded = s2[right]                           # update the state, by making sure if the adding, represented a new match
        map2[letterAdded] += 1
        if map1[letterAdded] == map2[letterAdded]:
            matches += 1
        elif map1[letterAdded] == map2[letterAdded] - 1:  # or if it represented one less match (compare the status before the add)
            matches -= 1

        letterRemoved = s2[left]
        map2[letterRemoved] -= 1
        if map1[letterRemoved] == map2[letterRemoved]:       # update the state, by making sure if the removal, represented a new match
            matches += 1
        elif map1[letterRemoved] == map2[letterRemoved] + 1: # or if it represented one less match (compare the status before the rem)
            matches -= 1

        left += 1
        right += 1

    return matches == 26 # must return the comparison


print(checkInclusion('ab', 'idbaooo'))