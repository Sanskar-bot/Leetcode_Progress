# ============================================================
#  Problem : Number of Provinces
#  URL     : https://leetcode.com/problems/number-of-provinces/
#  Solution: https://leetcode.com/solutions/dfs-with-visited-array-count-connected-g-tbgr/
#  Date    : 2026-11-03
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Cities that are directly or indirectly connected form one province. If I start a search from an unvisited city and visit everything reachable from it, that search covers exactly one province. So the number of provinces is the number of times I have to start a new search.

# Approach
1. Keep a `visited` list, one flag per city.
2. `dfs(city)` returns if the city is already visited. Otherwise it marks the city and calls `dfs` on every city connected to it (`isConnected[city][con] == 1`).
3. Loop over all cities. If a city is not visited, it belongs to a new province, so call `dfs(city)` and add 1 to `count`.
4. Return `count`.

Each search marks a whole province as visited, so no province is counted twice.

# Complexity
- Time complexity: $$O(n^2)$$, because every city scans its full row of the matrix once.

- Space complexity: $$O(n)$$ for the `visited` list and the recursion stack.

# Code

# --- CODE ---
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n

        def dfs(city):
            if visited[city] == True:
                return
            visited[city]=True
            for con in range(n):
                if isConnected[city][con] == 1 and not visited[con]:
                    dfs(con)
        count =0

        for city in range (n):
            if visited[city]== False:
                dfs(city)
                count+=1

        return count

