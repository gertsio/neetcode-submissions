import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       hash_map = {}
       output = []

       for num in nums:
         if num in hash_map:
            hash_map[num] += 1 
         else:
            hash_map[num] = 1
      
       for key, frequency in hash_map.items():
        heapq.heappush(output, (frequency, key))

        if len(output) > k:
            heapq.heappop(output)

       return [key for frequency, key in output]