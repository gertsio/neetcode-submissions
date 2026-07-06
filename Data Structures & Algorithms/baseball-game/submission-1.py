class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum_stack = []

        for i in range(len(operations)): 
            if operations[i] == "+":
               plus_operation = sum_stack[-1] + sum_stack[-2]
               sum_stack.append(plus_operation)
            elif operations[i] == "C":
                sum_stack.pop()
            elif operations[i] == "D":
                sum_stack.append(int(sum_stack[-1] * 2))    

            else:
                sum_stack.append(int(operations[i]))
        
        return sum(sum_stack)