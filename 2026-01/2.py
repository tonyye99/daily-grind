# 961. N-Repeated Element in Size 2N Array
# Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02
# Time: 10+
# Solved: Yes

# TIL: can do easily with hashmap/set but O(b) space/time.
# Approach-2: since the duplicated element is 2n array length, can only iterate window 1-3.
# if 1 element is duplicated, then the first and second element are the same.
# if 2 elements are duplicated, num length -> 2 * 2 = 4, so iterate window 1-3 and return if dup is found else it is sure nums[-1]