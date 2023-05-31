# https://leetcode.com/problems/3sum/description/
# Variation of: # https://www.algoexpert.io/questions/three-number-sum with targetSum = 0

# input: [-1,0,1,2,-1,-4]
# output: [[-1,-1,2],[-1,0,1]]
#          ^ Not repeated triplets

def threeSum(nums):
    nums.sort()     # O(n log(n)) Time
    triplets = []

    for i in range(len(nums) - 2):  # We stop at the ante-penultimate, we're inspecting one num against 2 to the right
        left = i + 1
        right = len(nums) - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == 0: # Triplet found!
                if [nums[i], nums[left], nums[right]] not in triplets:
                    triplets.append([nums[i], nums[left], nums[right]])     # Only append if triplet not exists yet
                # In any case, move the pointers to keep exploring the string/array
                left += 1
                right -= 1

            elif currentSum < 0:    # Increment left pointer garantees a larger currentSum
                left += 1
            
            elif currentSum > 0:    # Decrement the left pointer guarantees a smaller currentSum
                right -= 1

    return triplets


# O(n log(n)) Time
# O(1) Space


threeSum([-1,0,1,2,-1,-4])