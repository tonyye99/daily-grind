# 944. Delete Columns to Make Sorted
# Link: https://leetcode.com/problems/delete-columns-to-make-sorted/description/?envType=daily-question&envId=2025-12-20
# Time: 40+
# Solved: No 

# TIL: Start comparing from the index 1, if strs[row][col] < strs[row-1][col], then increase and break because no need to compare further.
# since starting from index 1, can compare to the end with its previous row.
# Also, this is not [row][col] looping, it's [col][row] 

# Another easier approah, use zip to compare the columns and check if they are sorted.
# It will be useful for #955