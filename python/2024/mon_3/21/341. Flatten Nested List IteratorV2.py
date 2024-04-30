from typing import List


class NestedIterator:
    def __init__(self, nestedList: List[int | list]):
        """
        这里将会使用栈来实现，出栈之后就恢复数据，类似进程切换的时候寄存器回复状态
        在这里我没有使用前面使用的定义的那个 class，这里的代码更加简洁，高效
        T(n): O(1) # n 表示的是实际的数字的数量
        S(n): O(n) # 取决于 stack 的长度
        """
        # 第一个表示的是 _stack: [(now_index, now_list)]
        # 先取出现在 cur 指向的数字，然后再将 cur 下移
        self._stack = []
        self._now_cur = 0
        self._now_list = nestedList
        self._init_len = len(nestedList)

    # 每一个 next 执行之前都应该判定到底有没有 next
    def next(self) -> int:
        # 当前指向的事 integer
        if isinstance(self._now_list[self._now_cur], int):
            des_num = self._now_list[self._now_cur]
            self._now_cur += 1
            if self._now_cur == len(self._now_list) and len(self._stack) > 0:
                self._now_cur, self._now_list = self._stack.pop()
            return des_num
        # 当前指向的是 list
        else:
            if self._now_cur + 1 < len(self._now_list):
                self._stack.append((self._now_cur + 1, self._now_list))
            self._now_list = self._now_list[self._now_cur]
            self._now_cur = 0
            return self.next()

    def hasNext(self) -> bool:
        if self._now_cur == len(self._now_list) and \
                ((len(self._stack) == 1 and self._stack[-1][0] == self._now_list) or (len(self._stack) == 0)):
            return False
        return True


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
if __name__ == "__main__":
    n = NestedIterator([1, 2, [3, [4, [5, [6, [7, 8, 9, 10]]]]]])
    while n.hasNext():
        print(n.next())
