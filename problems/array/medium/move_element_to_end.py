# https://www.algoexpert.io/questions/move-element-to-end
# input: 
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2

# output:
# [1, 3, 4, 2, 2, 2, 2, 2]

def moveElementToEnd(array, toMove):
    # Pointer for array from left-most element
    i = 0
    # Pointer for array from right-most element
    j = len(array) - 1

    # While both pointers don't pass each other
    while i < j:
        leftNum = array[i]
        rightNum = array[j]

        if leftNum == toMove:
            if rightNum != toMove:
                # Swap values and keep inspecting values to the right
                array[i] = rightNum
                array[j] = leftNum
                i += 1
            # If rightNum cannot be replaced (because it is equal to toMove)
            # Keep inspecting values to the left, so they can be replaced
            j -= 1

        # leftNum != toMove
        else:
            i += 1

    return array

# O(n) T
# O(1) S