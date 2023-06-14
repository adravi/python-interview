"""
Max Game Points
Question
In a video game a player starts at the beginning of a maze,
and there are several paths that can take them to the next level of the game.
Each path has one or more milestones where the player gets one or more points for passing them.
What's the maximum number of points our player can get?

         1
       / | \
      /  8  \
     /  / \  \
    1  2   4  3
   / \       / 
  5  10     7 

find_max_points(game) => 12
"""

def find_max_points(node):
    if not node.children:
        return node.points

    return node.points + max(find_max_points(child) for child in node.children)

class Milestone(object):
    def __init__(self, points, children=None):
        self.points = points
        self.children = children or []

game = Milestone(1, [
    Milestone(1, [
        Milestone(5),
        Milestone(10)
    ]),
    Milestone(3, [
        Milestone(7)
    ])
])
  
print(find_max_points(game))