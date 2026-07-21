class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        postfix = 1
        prefix = 1

        for i in range(len(nums)):
            output.append(prefix)
            prefix = prefix * nums[i]

        for i in range(len(nums) -1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]

        return output 
