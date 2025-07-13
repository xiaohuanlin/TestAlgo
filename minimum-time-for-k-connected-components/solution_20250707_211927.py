# 文件名: solution
# 题目: Minimum Time for K Connected Components

## Solution
```python3
class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.cnt = n

    def find(self, u):
        i = u
        while self.roots[i] != i:
            i = self.roots[i]
        while self.roots[u] != i:
            u = self.roots[u]
            self.roots[u] = i
        return i
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.roots[root_u] > self.roots[root_v]:
            self.roots[root_v] = root_u
            self.rank[root_u] += self.rank[root_v]
        else:
            self.roots[root_u] = root_v
            self.rank[root_v] += self.rank[root_u]
        self.cnt -= 1
    

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if len(edges) == 0:
            return 0 if n >= k else -1
        edges.sort(key=lambda x: x[2], reverse=True)
        uf = UnionFind(n)
        ans = edges[0][2]
        for u, v, t in edges:
            uf.union(u, v)
            if uf.cnt < k:
                return t
        return 0


```

## Metadata
- Status: Accepted
- Language: python3
- Submit Time: 2025-07-07 21:19:27
- Runtime: 129 ms
- Memory: 60.2 MB