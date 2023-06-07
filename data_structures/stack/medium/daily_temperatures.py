# https://leetcode.com/problems/daily-temperatures/

# input: temps = [73,74,75,71,69,72,76,73]
# output: [1,1,4,2,1,1,0,0]

def dailyTemperatures(temps):
    answer = [0] * len(temps) # We know that for the last values, we will have zeros

    # The trick is to have a value-decreasing stack
    tempsStack = [] # each element is a pair [tempValue, tempIndex]
                    # tempsStack[-1]     -> pair on top of stack
                    # tempsStack[-1][0]  -> first element of pair on top: tempValue
                    # tempsStack[-1][1]  -> scond element of pair on top: tempIndex

    for i, currentTemp in enumerate(temps):
        # If there is at least one pair on the stack AND the tempValue is larger than the currentTemp
        while tempsStack and currentTemp > tempsStack[-1][0]:
            tempValue, tempIndex = tempsStack.pop() # Remove the pair and use the index to calc the diff between indexes
            answer[tempIndex] = i - tempIndex       # That is the number of days before a higher temp
        
        # If the curentTemp is not larger, then simply append (value, index) to the stack
        tempsStack.append([currentTemp, i])

    return answer
        
# O(n) Time
# O(n) Space
