class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev, self.next = prev, next

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        prev_temp = self.tail.prev
        self.tail.prev = ListNode(value, prev_temp, self.tail)
        prev_temp.next = self.tail.prev

    def appendleft(self, value: int) -> None:
        next_temp = self.head.next
        self.head.next = ListNode(value, self.head, next_temp)
        next_temp.prev = self.head.next

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        val = last_node.val
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev

        return val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        target_node = self.head.next
        value = target_node.val
        next_node = target_node.next
        target_node.next.prev = self.head

        self.head.next = next_node
        next_node.prev = self.head
        
        return value
        
