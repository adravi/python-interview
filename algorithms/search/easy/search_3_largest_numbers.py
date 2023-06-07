# https://www.algoexpert.io/questions/find-three-largest-numbers

def findThreeLargestNumbers(array):
    threeLargestNums = [None, None, None]
    
    for num in array:
        updateLargest(threeLargestNums, num)
    
    return threeLargestNums

def updateLargest(largestNums, num):
    if not largestNums[2] or num > largestNums[2]:
        updateAndShift(largestNums, num, 2)
    elif not largestNums[1] or num > largestNums[1]:
        updateAndShift(largestNums, num, 1)
    elif not largestNums[0] or num > largestNums[0]:
        updateAndShift(largestNums, num, 0)

def updateAndShift(largestNums, num, idx):
    for i in range(idx + 1):
        if i == idx:
            largestNums[i] = num
        else:
            largestNums[i] = largestNums[i + 1]

# O(n) Time
# O(1) Space
