class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MODULE = 10 ** 9 + 7
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        maxHorizontalGap = max([horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts))]) % MODULE
        maxVerticalGap = max([verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts))]) % MODULE
        return (maxHorizontalGap * maxVerticalGap) % MODULE