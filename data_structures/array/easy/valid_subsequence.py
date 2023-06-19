# https://www.algoexpert.io/questions/validate-subsequence

# input:
# 1) array = [1, 2, 3, 4], sequence = [1, 3, 4]
# 2) array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [1, 6, -1, 10]

def is_valid_subsequence(array, sequence):
    i = 0
    j = 0
    
    for i in range(len(array)):
        if array[i] == sequence[j]:
            j += 1

        if j == len(sequence):
            return True
    
    return False

# O(n) time
# O(1) space