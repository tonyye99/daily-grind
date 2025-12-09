# 1925. Count Special Triplets 
# Link: https://leetcode.com/problems/count-special-triplets/editorial/?envType=daily-question&envId=2025-12-09
# Time: 40+ mins
# Solved: No

# TIL: two counts
# total count, count all occurances of nums
# left count, count it on the go, then right count = total count - left count
# ans += right count * left count
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # count = 0

        # for i in range(len(nums)):
        #     half = nums[i] // 2
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == half:
        #             for k in range(j + 1, len(nums)):
        #                 if nums[k] == nums[i]:
        #                     count += 1
        
        # return count
        
        return 0