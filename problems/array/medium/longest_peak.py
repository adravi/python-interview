# https://www.algoexpert.io/questions/longest-peak
# input: array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]]
# output: 6 // 0, 10, 6, 5, -1, -3

def longestPeak(array):
    if len(array) < 3:
        return 0

    peakIndexes = []
    for idx in range(1, len(array) - 1):
        potentialPeak = array[idx]
        left = array[idx - 1]
        right = array[idx + 1]

        if potentialPeak > left and potentialPeak > right:
            peakIndexes.append(idx)

    longestPeak = 0
    for peakIdx in peakIndexes:
        length = 1
        i, j = peakIdx, peakIdx 

        while i - 1 >= 0:
            current = array[i]
            prev = array[i - 1]
            if current <= prev:
                break
            length += 1
            i -= 1

        while j + 1 < len(array):
            current = array[j]
            next = array[j + 1]
            if current <= next:
                break
            length += 1
            j += 1
        
        if length > longestPeak:
            longestPeak = length

    return longestPeak

# O(n) time
# O(s) space