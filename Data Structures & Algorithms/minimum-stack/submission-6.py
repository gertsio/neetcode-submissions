class MinStack:

    def __init__(self):
        self.min_stack = [] #[-2,]
        self.min_values = [] #[]

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if not self.min_values:
          self.min_values.append(val)
        else:
          if self.min_values[-1] >= val:
            self.min_values.append(val)

    def pop(self) -> None:
        deleted = self.min_stack.pop()
        if deleted == self.min_values[-1]:
            self.min_values.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]