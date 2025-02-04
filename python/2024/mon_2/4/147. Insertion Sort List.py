from python.util.core.list_util import *


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        嗯...算法的核心是保证时间复杂度和空间复杂度最低
        T(n): O(n**n)
        S(n): O(1)
        :param head:
        :return:
        """
        if head is None:
            return None
        # 头指针
        p: ListNode = head
        # 需要排序的元素
        insert_pre: ListNode = head
        cut: Optional[ListNode] = None
        while insert_pre.next is not None:
            if insert_pre.next.val <= head.val:
                cut = insert_pre.next
                insert_pre.next = insert_pre.next.next
                cut.next = head
                head = cut
            else:
                if insert_pre.next.val >= insert_pre.val:
                    insert_pre = insert_pre.next
                    continue
                p: ListNode = head
                while p is not None:
                    if p.val < insert_pre.next.val <= p.next.val:
                        cut: ListNode = insert_pre.next
                        insert_pre.next = insert_pre.next.next
                        cut.next = p.next
                        p.next = cut
                        break
                    else:
                        p = p.next
        return head


if __name__ == "__main__":
    arr_ini = [4, 2, 1, 3, 5, 6, 0, -1]
    head = arr2list(arr_ini)
    print(list2arr(Solution().insertionSortList(head)))
