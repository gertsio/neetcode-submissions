class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       hash_map = {}
       output = []

       for num in nums:
         if num in hash_map:
            hash_map[num] += 1 
         else:
            hash_map[num] = 1

       new_sorted = sorted(
         hash_map.items(),
         key = lambda pair: pair[1],
         reverse = True
       )  

       for i in range(k):
        output.append(new_sorted[i][0])
       return output