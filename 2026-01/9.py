# 865. Smallest Subtree with all the Deepest Nodes
# Link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09
# Time: 40+ 
# Solved: Yes

# TIL: DFS. find the deepest nodes, compare left and right if equal, return current node. else return the deeper node.

# related: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# this one is similar but no need to find the deepest nodes (since given).
# the difference is need to find the deepest node + need to find the parent of the deepest node.