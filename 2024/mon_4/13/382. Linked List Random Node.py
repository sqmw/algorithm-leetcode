# Definition for singly-linked list.
import random
from typing import Optional

from util.core import list_util


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    T(n): O(1)
    S(n): O(1)
    """

    def __init__(self, head: Optional[ListNode]):
        self._head = head
        self._now = self._head

    def getRandom(self) -> int:
        # 目前我的方法是每次都均衡向下走一步
        # 但是其实可以随机走 0-n 步[下面将 n 选择为 4]
        # 每次赋值之前需要保证 _now not None
        _step = random.randint(0, 4)
        for _ in range(_step):
            self._now = self._now.next if self._now.next is not None else self._head
        return self._now.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

if __name__ == "__main__":
    s = Solution(list_util.arr2list([1, 2, 3]))
    print(s.getRandom())
    print(s.getRandom())
    print(s.getRandom())
    print(s.getRandom())
    print(s.getRandom())
    print(s.getRandom())
