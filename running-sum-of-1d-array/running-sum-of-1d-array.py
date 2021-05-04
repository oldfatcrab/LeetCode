class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        for i in range(len(nums)):
            nums[i] += total
            total = nums[i]
        return nums