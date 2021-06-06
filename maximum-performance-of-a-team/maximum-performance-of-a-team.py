from heapq import heappush, heappop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        efficiencySpeedPairs, heap, sum, performance = sorted(zip(efficiency, speed), reverse = True), [], 0, 0
        for efficiency, speed in efficiencySpeedPairs:
            if len(heap) > k - 1:
                sum -= heappop(heap)
            heappush(heap, speed)
            
            sum += speed
            performance = max(performance, sum * efficiency)
        return performance % (10 ** 9 + 7)