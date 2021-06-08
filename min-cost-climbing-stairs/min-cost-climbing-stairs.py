class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [0, 0]
        for i in range(len(cost)):
            costs[i % 2] = min(costs) + cost[i]
        return min(costs)