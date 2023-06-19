# https://leetcode.com/problems/generate-parentheses/
# input: n = 3
# output: ["((()))","(()())","(())()","()(())","()()()"]  <- observe the patterns and come up with rules for closing validly

# 1) only add open parenthesis if open < n
# 2) only add close parenthesis if closed < n
# 3) IIF close == open == n, a VALID combination has been found

                                                            # Combinations generation can be seen as a DFS recursivetraversal 
def generate_parenthesis(n):                                # see image:
    res = []                                                    
                                                                # solution is easier to understand WITHOUT USING A STACK
    
    def backtrack(open_n, closed_n, combination):               # internal backtracking function to be called RECURSIVELY
        
        if open_n == closed_n == n:                             # 3rd rule: a VALID combination has been reached
            res.append(combination)
            return
    
        if open_n < n:                                          # 1st rule: we can append one more '(' opening parenthesis
            backtrack(open_n + 1, closed_n, combination + "(")  # call the backtrack function, updating the open_n by 1
            
        if closed_n < open_n:                                   # 2nd rule: we can append one more ')' opening parenthesis
            backtrack(open_n, closed_n + 1, combination + ")")  # call the backtrack function, updating the closed_n by 1
            
    backtrack(0, 0, "")  # don't forget the initial call
    return res

# O(n) time
# O(1) space // no extra aux memory was used, however the string concatenation is an expensive operation (new mem fo each string)

# explanation: https://www.youtube.com/watch?v=s9fokUqJ76A&ab_channel=NeetCode
# see 


generate_parenthesis(3)

