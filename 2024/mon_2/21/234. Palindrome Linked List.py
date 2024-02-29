import math
from typing import Optional

from util.core import list_util
from util.core.list_util import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        T(n): O(n) /// 2.5 * n
        S(n): O(1)
        """
        now_len = 0
        p = head
        # 计算得到链表长度
        while p is not None:
            now_len += 1
            p = p.next
        if now_len < 2:
            return True
        half = math.ceil(now_len / 2)
        now_len = 1
        p = head
        # 链表指针 p 滑动到下半截链表开始位置的前一个位置
        while now_len < half:
            p = p.next
            now_len += 1
        q = p.next.next
        if p.next.next is not None:
            p.next.next = None
        # 将 p 之后的全部反转
        while q is not None:
            q_next = q.next
            t = p.next
            p.next = q
            q.next = t
            q = q_next

        q = p.next
        p = head
        # 判定是否想等
        while q is not None:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(list_util.arr2list([1, 1, 2, 1])))
