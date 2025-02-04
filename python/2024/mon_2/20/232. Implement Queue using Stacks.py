class MyQueue:

    def __init__(self):
        self._stack = []
        self._temp_stack2out = []

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        while len(self._stack) > 0:
            self._temp_stack2out.append(self._stack.pop())
        des_val = self._temp_stack2out.pop()
        while len(self._temp_stack2out) > 0:
            self._stack.append(self._temp_stack2out.pop())
        return des_val

    def peek(self) -> int:
        return self._stack[0]

    def empty(self) -> bool:
        return len(self._stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
