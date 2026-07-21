from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for index in range(len(nums)):
            numbers_except_current = nums[:index] + nums[index + 1:]
            output.append(prod(numbers_except_current))

        return output