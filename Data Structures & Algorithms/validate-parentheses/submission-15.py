class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")":"(", 
            "}":"{",
            "]":"["
            }

        open_brackets = {"(", "{", "["}
        
        stack = []

        for char in s:
         if char in open_brackets:
            stack.append(char)
         else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        return not stack 



