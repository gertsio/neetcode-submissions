from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        res = False
        for num in nums:
            if cnt[num] > 1:
                res = True
        return res
                
