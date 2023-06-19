# https://www.algoexpert.io/questions/longest-peak
# input: array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]]
# output: 6 // 0, 10, 6, 5, -1, -3

def longest_peak(array):
    if len(array) < 3:
        return 0

    peak_indexes = []
    for idx in range(1, len(array) - 1):
        potential_peak = array[idx]
        left = array[idx - 1]
        right = array[idx + 1]

        if potential_peak > left and potential_peak > right:
            peak_indexes.append(idx)

    longest_peak = 0
    for peak_idx in peak_indexes:
        length = 1
        i, j = peak_idx, peak_idx 

        while i - 1 >= 0:
            curr = array[i]
            prev = array[i - 1]
            if curr <= prev:
                break
            length += 1
            i -= 1

        while j + 1 < len(array):
            curr = array[j]
            next = array[j + 1]
            if curr <= next:
                break
            length += 1
            j += 1
        
        if length > longest_peak:
            longest_peak = length

    return longest_peak

# O(n) time
# O(s) space