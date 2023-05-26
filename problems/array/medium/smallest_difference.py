# https://www.algoexpert.io/questions/smallest-difference
# input:
# arrayOne = [-1, 5, 10, 20, 28, 3] -> size n
# arrayTwo = [26, 134, 135, 15, 17] -> size m

def smallestDifference(arrayOne, arrayTwo):
    # Sort both arrays! That's the key for this type of problems! 
    # This implies a complexity if O(n log(n)) but that's better than O(n^2), the brute force approach
    arrayOne.sort()
    arrayTwo.sort()
    
    # Pointers to move across both arrays
    i = 0
    j = 0

    # Calculate the absolute distance between 2 integers
    distance = float('inf')
    smallest = float('inf')
    smallestPair = []

    while i < len(arrayOne) and j < len(arrayTwo):
        a = arrayOne[i]
        b = arrayTwo[j]

        distance = abs(a - b)
        if distance < smallest:
            smallest = distance
            smallestPair = [a, b]

        # Move the pointer of the second array to the right, since a is bigger
        if a > b:
            j += 1
        # Move the pointer of the first array to the right, since b is bigger
        elif a < b:
            i += 1
        # a == b and the distance is zero, so nothing is gonna be smaller than that
        else:
            return [a, b]

    return smallestPair

# O(n log(n) + m log(m)) Time
# O(n + m) Space

