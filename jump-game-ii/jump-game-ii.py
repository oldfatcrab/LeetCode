class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = list(range(len(nums)))
        for i, num in enumerate(nums):
            for j in range(i + 1, min(i + num + 1, len(nums))):
                jumps[j] = min(jumps[j], jumps[i] + 1)
        return jumps[-1]