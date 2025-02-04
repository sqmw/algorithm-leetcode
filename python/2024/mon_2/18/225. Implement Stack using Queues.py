from collections import deque


class MyStack:
    """
    挺无语的，为了出题而出题
    """

    def __init__(self):
        self.queue_stack = deque()
        self.temp_queue = deque()

    def push(self, x: int) -> None:
        self.temp_queue.append(x)
        while len(self.queue_stack) > 0:
            self.temp_queue.append(self.queue_stack.popleft())
        t = self.queue_stack
        self.queue_stack = self.temp_queue
        self.temp_queue = t

    def pop(self) -> int:
        return self.queue_stack.popleft()

    def top(self) -> int:
        return self.queue_stack[0]

    def empty(self) -> bool:
        return len(self.queue_stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
