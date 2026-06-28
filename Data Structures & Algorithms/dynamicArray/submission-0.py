class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * self.capacity


    def get(self, i: int) -> int:
        if i < 0 or i >= self.length:
            raise IndexError("Index out of bounds")
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
      if i < 0 or i >= self.length:
        raise IndexError("Index out of bounds")
      self.arr[i] = n


    def pushback(self, n: int) -> None:
      if self.length == self.capacity:
        self.resize()
      self.arr[self.length] = n
      self.length += 1


    def popback(self) -> int:
      if self.length == 0:
        raise IndexError("Cannot pop from empty array")
      self.length -= 1
      val = self.arr[self.length]
      self.arr[self.length] = None
      return val
 

    def resize(self) -> None:
      newCapacity = self.capacity * 2
      newArr = [None] * newCapacity 
      for i in range(self.length):
        newArr[i] = self.arr[i]
      self.arr = newArr
      self.capacity = newCapacity


    def getSize(self) -> int:
      return self.length
        
    
    def getCapacity(self) -> int:
      return self.capacity