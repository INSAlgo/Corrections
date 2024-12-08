# https://practice.geeksforgeeks.org/problems/gold-mine-problem2608/1

class Solution:
    def maxGold(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        if n == 1:
            return sum(mat[0])
        
        dp = [mat[i][0] for i in range(n)]
        
        for j in range(1, m):
            next_dp = [0] * n
            next_dp[0] = max(dp[0], dp[1]) + mat[0][j]
            for i in range(1, n - 1):
                next_dp[i] = max(dp[i - 1], dp[i], dp[i + 1]) + mat[i][j]
            next_dp[n - 1] = max(dp[n - 2], dp[n - 1]) + mat[n - 1][j]
            dp = next_dp
        
        return max(dp)
