# LC: 1306. Jump Game III 
# Link: https://leetcode.com/problems/jump-game-iii/description/
# Time: 20 mins
# Solved: Yes

# Approach-1: DFS - time: O(n), space: O(n)
def canReach(self, arr: List[int], start: int) -> bool:
    visited = {}

    def dfs(i):
        # print(visited, i)
        if i >= len(arr) or i < 0 or (i in visited and visited[i] == arr[i]):
            return False
        if arr[i] == 0:
            return True
        
        visited[i] = arr[i]

        if dfs(i + arr[i]) or dfs(i - arr[i]):
            return True

        # visited[i]

        return False
    
    return dfs(start)