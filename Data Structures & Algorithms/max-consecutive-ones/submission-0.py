class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = []
        last_one = 0
        for i in range(len(nums)):
            if nums[i] == 1:  
                last_one += 1
                if i == len(nums) - 1: 
                    ones.append(last_one)
            else: 
                ones.append(last_one)
                last_one = 0

        return max(ones)