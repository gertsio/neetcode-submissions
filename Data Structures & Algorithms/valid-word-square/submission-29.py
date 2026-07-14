class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for row_index, word in enumerate(words):
            for column_index, char in enumerate(word):
                 if column_index < len(words) and row_index < len(words[column_index]):
                    if words[row_index][column_index] == words[column_index][row_index]:
                       continue
                    else:
                       return False
                 else:
                    return False
        return True    
        
        