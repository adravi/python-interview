# https://www.algoexpert.io/questions/three-number-sum

# input: [12, 3, 1, 2, -6, 5, -8, 6]
# output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

def threeNumberSum(array, targetSum):
    # Sort the array in-place! O(n log(n))
    array.sort()

    triplets = []

    # We stop at the aray lenght - 2, because we are inspecting one number agains 2 to the right
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        # Make sure the pointers are not overlapping/passing each other
        while left < right:
            currentSum = array[i] + array[left] + array[right]

            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1

            # Increment left pointer garantees a larger currentSum
            elif currentSum < targetSum:
                left += 1
                
            # Decrement the left pointer guarantees a smaller currentSum
            elif currentSum > targetSum:
                right -= 1

    return triplets

# O(n^2) Time
# O(n) Space

            