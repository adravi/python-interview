
# https://leetcode.com/problems/number-of-recent-calls/description/
# input: [[], [1], [100], [3001], [3002]]
# output: [null, 1, 2, 3, 3]

from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()        # remember: from collections import deque
        
    def ping(self, t: int) -> int:
        leftBoundary = t - 3000     # inclusive range: [t-3000, t]
        self.queue.append(t)        # add the time, no matter what

        while leftBoundary > self.queue[0]: # only check if the elements in queue fall within the range
            self.queue.popleft()            # elements are increasing, we only need to check the left boundary

        return len(self.queue)      # return the size of the queue
    
# O(n) time
# O(n) space
# ---------------------------------------------------------------------------

# from collections import deque

# init queue: myQueue = deque()

# add element: myQueue.append(element)

# remove element: myQueue.popleft()
