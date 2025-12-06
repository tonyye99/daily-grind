# LC Daily: Count Partitions with Even Sum Difference 
# Link: https://leetcode.com/problems/count-partitions-with-even-sum-difference/editorial/?envType=daily-question&envId=2025-12-05
# Time: 20 mins
# Solved: Yes

# approach-1 - prefix/postfix sums - time: O(n) space: O(n)
def countPartitions(self, nums: List[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]

    postfix_sum = [0] * n
    postfix_sum[n-1] = nums[n-1]

    for i in range(n-2, -1, -1):
        postfix_sum[i] = postfix_sum[i+1] + nums[i]
    
    ans = 0

    for i in range(n-1):
        if abs(prefix_sum[i] - postfix_sum[i + 1]) % 2 == 0:
            ans += 1


    return ans

# approach-2 - prefix/postfix sums (optimized) - time: O(n) space: O(1)
# @todo

# TIL: Mathematically, if total_sum is even, there are all partitions that works, 
# if total_sum is odd, there are no partition works
# approach-2 - math - time: O(n) space: O(1)
def countPartitions(self, nums: List[int]) -> int:
    total_sum = sum(nums)

    return len(nums) - 1 if total_sum % 2 == 0 else 0