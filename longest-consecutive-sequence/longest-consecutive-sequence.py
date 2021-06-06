class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result, nums, visited = 0, set(nums), set([])
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            left, right = num, num
            while left in nums:
                visited.add(left)
                left -= 1
            while right in nums:
                visited.add(right)
                right += 1
            result = max(result, right - left - 1)
        return result