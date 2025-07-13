# File: solution
# Problem: Minimum Time for K Connected Components
# Status: Wrong Answer
# Language: python3
# Submit Time: 2025-07-07 15:45:45
# Runtime: N/A
# Memory: N/A

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        maps = defaultdict(list)
        times = []
        for u,v,w in edges:
            times.append(w)
            maps[u].append(v)
            maps[v].append(u)

        visited = [False for _ in range(n)]
        def dfs(u):
            if visited[u]:
                return
            visited[u] = True
            for v in maps[u]:
                dfs(v)

        cnt = 0
        for i in range(n):
            if visited[i]:
                continue
            dfs(i)
            cnt += 1
        target = k - cnt
        times.sort()
        return times[target-1] if target > 0 else 0
