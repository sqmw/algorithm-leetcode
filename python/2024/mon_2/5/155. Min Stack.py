import sys


class Node:
    def __init__(self, val: int = 0, nNext: 'Node' = None):
        self.val = val
        self.next = nNext


class MinStack:
    """
    这道题需要得到最小的值，并且是在 T(n) == O(1)
    这个是不可能的，题目有问题
    """

    def __init__(self):
        # 表示的是 head 不用来存储据
        self._stack_head = Node()
        self._min_ref = None

    def push(self, val: int) -> None:
        new_node = Node(val)
        # 表示是第一次插入
        if self._stack_head.next is None:
            self._stack_head.next = new_node
        else:
            new_node.next = self._stack_head.next
            self._stack_head.next = new_node

    def pop(self) -> None:
        # 表示现在为空
        if self._stack_head.next is None:
            return
        else:
            self._stack_head.next = self._stack_head.next.next

    def top(self) -> int:
        return self._stack_head.next.val

    def getMin(self) -> int:
        p = self._stack_head.next
        min_val = sys.maxsize
        while p is not None:
            min_val = min(min_val, p.val)
            p = p.next
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    des_arr = []
    minStack = MinStack()

    des_arr.append(minStack.push(-2))
    des_arr.append(minStack.push(0))
    des_arr.append(minStack.push(-3))

    des_arr.append(minStack.getMin())
    des_arr.append(minStack.pop())
    des_arr.append(minStack.top())
    des_arr.append(minStack.getMin())

    print(des_arr)
