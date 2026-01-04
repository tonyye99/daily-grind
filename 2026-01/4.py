# 1390. Four Divisors
# Link: https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04
# Time: 50+
# Solved: Yes

# TIL: Math problem, find sum of divisors within loop. 
# catches: skip, if curr num is prime and skip if curr num is a perfect square because it will have duplicate divisors. 4 => 2,2
# while calculating sum of divisors, count the loop and break if count > 1 or return 0 because that number has more than 4 divisors.