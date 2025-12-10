# 3577. Count the Number of Computer Unlocking Permutations 
# Link: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/description/?envType=daily-question&envId=2025-12-10
# Time: 20+ mins
# Solved: No

# TIL: since nums[0] is the key, all the other numbers must be greater than nums[0]
# return the factorial of the length of the array - 1

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:

        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
        
        ans = 1
        mod = 10**9 + 7

        for i in range(2, len(complexity)):
            ans = ans * i % mod
        
        return ans