from heapq import heappush, heappop

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        h = []
        for n in target:
            heappush(h, -n)
        while h[0] != -1:
            num = -heappop(h)
            total -= num
            if num <= total or total < 1:
                return False
            num %= total
            total += num
            heappush(h, -num or -total)
        return True