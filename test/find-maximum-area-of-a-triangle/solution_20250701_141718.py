"""
Find Maximum Area of a Triangle



LeetCode Problem
"""

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        x = []
        y = []
        for i in range(len(coords)):
            x.append((coords[i][0], coords[i][1]))
            y.append((coords[i][1], coords[i][0]))
        x.sort()
        y.sort()
        res = -1
        for i in range(len(x)-1):
            if x[i][0] == x[i+1][0]:
                h = max(x[-1][0] - x[i][0], x[i][0] - x[0][0])
                res = max(res, abs(x[i][1] - x[i+1][1]) * h)
        for i in range(len(y)-1):
            if y[i][0] == y[i+1][0]:
                h = max(y[-1][0] - y[i][0], y[i][0] - y[0][0])
                res = max(res, abs(y[i][1] - y[i+1][1]) * h)
        return res

# Test cases
if __name__ == "__main__":
    # Add your test cases here
    pass
