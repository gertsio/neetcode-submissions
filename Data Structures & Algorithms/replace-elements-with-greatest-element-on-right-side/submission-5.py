class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        original = arr[:]  # Keep the original values

        for i in range(len(arr)):
            the_biggest_number = -1

            for k in range(i + 1, len(original)):
                if original[k] > the_biggest_number:
                    the_biggest_number = original[k]

            arr[i] = the_biggest_number

        return arr