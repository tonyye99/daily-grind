# 955. Delete Columns to Make Sorted II
# Link: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/?envType=daily-question&envId=2025-12-21
# Time: 15+
# Solved: No 

# TIL: it is similar to 944 but now we need to combine the previous rows 
# ["xga","xfb","yfa"] -> first, xxy is sorted, second, xg,xf,yf is not sorted so remove/skipped it. 
# then xa, xb, ya is sorted so ans is 1.

# use zip(*strs) to unzip the string arrays and pairs -> ("x", "x", "y")
# then add to previous strings, eg for secondth loop since xxy is valid it will be added, prev=["x", "x", "y"] + curr -> ("g", "f", "f") -> ["xg", "xf", "yf"]
# if sorted then add to prev else increase the ans count (don't add) and return ans count.
# ["xg", "xf", "yf"] is not sorted so after third loop -> ["xa", "xb", "ya"]