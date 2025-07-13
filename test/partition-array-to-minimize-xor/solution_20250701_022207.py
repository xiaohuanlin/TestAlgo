"""
Partition Array to Minimize XOR



LeetCode Problem
"""

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] ^ nums[i])
        
        dp = [[float('inf') for _ in range(len(nums) + 1)] for _ in range(k)]
        dp[0] = presum[:]
        for i in range(k):
            dp[i][0] = float('inf')

        for i in range(1, k):
            for j in range(1, len(nums)+1):
                for m in range(i-1, j):
                    res = presum[j] ^ presum[m]
                    if res > dp[i][j]: 
                        continue
                    dp[i][j] = min(dp[i][j], max(dp[i-1][m], res))
        return dp[-1][-1]

# Test cases
if __name__ == "__main__":
    # Add your test cases here
    pass
