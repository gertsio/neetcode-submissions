class Solution:
    def isValid(self, s: str) -> bool:
        parantesis_keys_and_values = {
            ")":"(", 
            "}":"{",
            "]":"["
            }
        output = []

        for i in s:
         if i in parantesis_keys_and_values.values():
            output.append(i)
         elif len(output):
            if parantesis_keys_and_values[i] == output[-1]:
              output.pop()
            else:
                return False
         else: 
            return False
        return len(output) == 0 