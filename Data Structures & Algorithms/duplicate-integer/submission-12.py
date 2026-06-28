class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        i = 0
        while i < len(sortedNums) - 1:
            if sortedNums[i] == sortedNums[ i + 1]:
                return True
            i += 1
        return False     
