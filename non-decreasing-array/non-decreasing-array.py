class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        occured = (nums[1] < nums[0])
        for i in range(2, len(nums)):
            if nums[i] >= nums[i - 1]:
                continue
            if occured:
                return False
            occured, condition = True, int(nums[i] < nums[i - 2])
            nums[i - 1 + condition] = nums[i - condition]
        return True
