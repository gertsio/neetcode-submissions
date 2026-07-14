class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row, word in enumerate(words):
            for column, char in enumerate(word):
                if (
                    column >= len(words)
                    or row >= len(words[column])
                    or char != words[column][row]
                ):
                    return False

        return True