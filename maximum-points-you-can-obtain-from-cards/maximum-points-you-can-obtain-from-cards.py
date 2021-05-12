class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        currPoint = sum(cardPoints[:k])
        result = currPoint
        for i in range(k)[::-1]:
            currPoint += cardPoints[i - k] - cardPoints[i]
            result = max(result, currPoint)
        return result