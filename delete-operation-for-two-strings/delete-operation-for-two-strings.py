class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[0] * l2 for _ in range(l1)]
        for i in range(l1):
            for j in range(l2):
                dp[i][j] = (i or j) if i * j == 0 else (dp[i - 1][j - 1] if (word1[i - 1]) == word2[j - 1] else (min(dp[i - 1][j], dp[i][j - 1]) + 1))
        return dp[-1][-1]