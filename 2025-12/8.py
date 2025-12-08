# 1925. Count Square Sum Triples 
# Link: https://leetcode.com/problems/count-square-sum-triples/description/?envType=daily-question&envId=2025-12-08
# Time: 20 mins
# Solved: No

# TIL: If a**2 + b**2 = c**2, then c = sqrt(a**2 + b**2), eg-> 3**2 + 4**2 = 25 = sqrt(25) = 5 then c is 5
# so can check by calculating c first and then check if a**2 + b**2 = c**2
# c should be <= n because c is the max value of the triple

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = int((a*a + b*b) ** 0.5)
                if c <= n and (a*a + b*b) == c*c:
                    count += 1
        
        return count
        