# LC Daily: Count Collisions on a Road 
# Link: https://leetcode.com/problems/count-collisions-on-a-road/editorial/?envType=daily-question&envId=2025-12-04
# Time: 45 mins
# Solved: Yes

# unoptimized
class Solution:
    def countCollisions(self, directions: str) -> int:
        sCount = 0
        for i, d in enumerate(directions):
            if d == "R":
                s = False
                j = i
                while j < len(directions) - 1 and directions[j + 1] == "L":
                    if s == False: 
                        sCount += 2
                    else:
                        sCount += 1
                    s = True
                    j += 1
                j = i
                while s == True and j > 0 and directions[j - 1] == "R":
                    sCount += 1
                    j -= 1
            if d == "S":
                j = i
                while j > 0 and directions[j - 1] == "R":
                    sCount += 1
                    j -= 1
                j = i
                while j < len(directions) - 1 and directions[j + 1] == "L":
                    sCount += 1
                    j += 1

        return sCount


# TIL: if c is moving to right, increase by 1 (chance to hit)
#   if c is s (stationary), add increased chances
#  if c is moving to left, add increased chances + 1
# initially set chance = -1 and set chance to 1 in the first c == R
# R -> R -> R -> L = 1 -> 2 -> 3 -> result += 3 (chances) + 1 = 4

