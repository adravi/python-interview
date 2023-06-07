# https://www.algoexpert.io/questions/three-number-sum

# input: [12, 3, 1, 2, -6, 5, -8, 6]
# output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

def threeNumberSum(array, targetSum):
    # Sort the array in-place! O(n log(n))
    array.sort()

    triplets = []
    for i in range(len(array) - 2):     # We stop at the ante-penultimate, we are inspecting one number agains 2 to the right
        left = i + 1
        right = len(array) - 1

        while left < right:     # Make sure the pointers are not overlapping/passing each other
            currentSum = array[i] + array[left] + array[right]

            if currentSum == targetSum: # Triplet found!
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1

            elif currentSum < targetSum:    # Increment left pointer garantees a larger currentSum
                left += 1
            
            elif currentSum > targetSum:    # Decrement the left pointer guarantees a smaller currentSum
                right -= 1

    return triplets

# O(n^2) Time
# O(n) Space

            