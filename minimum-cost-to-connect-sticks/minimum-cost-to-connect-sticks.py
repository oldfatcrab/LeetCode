from heapq import heappush, heappop, heapify
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        result = 0
        while len(sticks) > 1:
            s = heappop(sticks) + heappop(sticks)
            result += s
            heappush(sticks, s)
        return result