# File: solution
# Problem: Minimum Increments to Equalize Leaf Paths
# Status: Wrong Answer
# Language: python3
# Submit Time: 2025-07-03 21:07:17
# Runtime: N/A
# Memory: N/A

class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        m = defaultdict(list)
        for u, v in edges:
            m[u].append(v)

        def dfs(node, parent):
            maxv = 0
            maxc = 0
            cnt = 0
            for v in m[node]:
                if v == parent:
                    continue
                cnt += 1
                changed, total = dfs(v, node)
                if maxv < total:
                    maxv = cost[v]
                    maxc = 1
                elif maxv == total:
                    maxc += 1
            return cnt - maxc, maxv + cost[node]

        return dfs(0, None)[0]