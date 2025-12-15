# 2110. Number of Smooth Descent Periods of a Stock
# Link: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/?envType=daily-question&envId=2025-12-15
# Time: 40+ mins
# Solved: No but (partially solved)

# TIL: formula is n * (n - 1) // 2
# 3 -> 3
# 4 -> 6
# 5 -> 10
# 6 -> 15
# 7 -> 21
# after each consecutive count, ans += formula(count)
# if count > 1, that means multiple smooth descent periods, so add into ans again. And return ans + len(prices)