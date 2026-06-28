class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumValue = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimumValue:
            self.minimumValue.append(val)
        elif val <= self.minimumValue[-1]:
            self.minimumValue.append(val)
        

    def pop(self) -> None:
        if self.stack[-1] == self.minimumValue[-1]:
            self.minimumValue.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        print('yo: ', self.minimumValue)
        return self.minimumValue[-1]
        
