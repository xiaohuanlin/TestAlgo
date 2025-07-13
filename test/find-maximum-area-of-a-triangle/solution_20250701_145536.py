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
        for i in range(len(x)):
            j = i
            while j < len(x) and x[i][0] == x[j][0]:
                j += 1
            if j == i + 1:
                continue
            h = max(x[-1][0] - x[i][0], x[i][0] - x[0][0])
            if h == 0:
                continue
            res = max(res, abs(x[i][1] - x[j-1][1]) * h)

        for i in range(len(y)):
            j = i
            while j < len(y) and y[i][0] == y[j][0]:
                j += 1
            if j == i + 1:
                continue
            h = max(y[-1][0] - y[i][0], y[i][0] - y[0][0])
            if h == 0:
                continue
            res = max(res, abs(y[i][1] - y[j-1][1]) * h)
        return res

# Test cases
if __name__ == "__main__":
    # Add your test cases here
    pass
