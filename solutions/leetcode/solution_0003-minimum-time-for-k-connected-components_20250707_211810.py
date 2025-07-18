"""
Minimum Time for K Connected Components

You are given an integer
n
and an undirected graph with
n
nodes labeled from 0 to
n - 1
. This is represented by a 2D array
edges
, where
edges[i] = [u
i
, v
i
, time
i
]
indicates an undirected edge between nodes
u
i
and
v
i
that can be removed at
time
i
.
You are also given an integer
k
.
Initially, the graph may be connected or disconnected. Your task is to find the
minimum
time
t
such that after removing all edges with
time <= t
, the graph contains
at least
k
connected components.
Return the
minimum
time
t
.
A
connected component
is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
Example 1:
Input:
n = 2, edges = [[0,1,3]], k = 2
Output:
3
Explanation:
Initially, there is one connected component
{0, 1}
.
At
time = 1
or
2
, the graph remains unchanged.
At
time = 3
, edge
[0, 1]
is removed, resulting in
k = 2
connected components
{0}
,
{1}
. Thus, the answer is 3.
Example 2:
Input:
n = 3, edges = [[0,1,2],[1,2,4]], k = 3
Output:
4
Explanation:
Initially, there is one connected component
{0, 1, 2}
.
At
time = 2
, edge
[0, 1]
is removed, resulting in two connected components
{0}
,
{1, 2}
.
At
time = 4
, edge
[1, 2]
is removed, resulting in
k = 3
connected components
{0}
,
{1}
,
{2}
. Thus, the answer is 4.
Example 3:
Input:
n = 3, edges = [[0,2,5]], k = 2
Output:
0
Explanation:
Since there are already
k = 2
disconnected components
{1}
,
{0, 2}
, no edge removal is needed. Thus, the answer is 0.
Constraints:
1 <= n <= 10
5
0 <= edges.length <= 10
5
edges[i] = [u
i
, v
i
, time
i
]
0 <= u
i
, v
i
< n
u
i
!= v
i
1 <= time
i
<= 10
9
1 <= k <= n
There are no duplicate edges.

LeetCode Problem
"""

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
        edges.sort(key=lambda x: x[2], reverse=True)
        uf = UnionFind(n)
        ans = edges[0][2]
        for u, v, t in edges:
            uf.union(u, v)
            if uf.cnt < k:
                return t
        return 0



# Test cases
if __name__ == "__main__":
    # Add your test cases here
    pass
