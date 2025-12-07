# LC: 1523. Count Odd Numbers in an Interval Range 
# Link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/?envType=daily-question&envId=2025-12-07
# Time: 10 mins
# Solved: Yes

# Approach-1: Math - time: O(1), space: O(1)
# TIL: I solved it with if-else conditon but this is more efficient
# odds nums can be count by up-to-x num + 1 // 2 because if x is even, it will exclude x else include x. 
# 0-7 -> (7+1)//2 = 3 -> 1,3,5,7 and 0-8 -> (8+1)//2 = 4 -> 1,3,5,7
def countOdds(self, low: int, high: int) -> int:
    return (high + 1) // 2 - low // 2