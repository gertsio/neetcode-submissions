from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for index, num in enumerate(nums): 
            res = [] 
            for index_second, num_second in enumerate(nums):
                
                if index_second == index:
                    res.append(1)
                else:
                    res.append(num_second)
            output.append(prod(res))

        return output

        