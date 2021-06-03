class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True
        for i in range(m):
            dp[i + 1][0] = (s1[:i + 1] == s3[:i + 1])
        for i in range(n):
            dp[0][i + 1] = (s2[:i + 1] == s3[:i + 1])

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = False
                if s1[i] == s3[i + j + 1]:
                    dp[i + 1][j + 1] = dp[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    dp[i + 1][j + 1] |= dp[i + 1][j]
        return dp[m][n]