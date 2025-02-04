# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        时间复杂度为 O(n)
        空间复杂度  O(n)
        涉及知识， hash id
        :param head:
        :return:
        """
        if head is None:
            return None
        p = head
        node_id_dic: dict[Node, Node] = {}
        head_new = Node(head.val)
        p_new = head_new
        # 建立映射关系
        while p is not None:
            if p.next is not None:
                p_new.next = Node(p.next.val)
            node_id_dic[p] = p_new
            p = p.next
            p_new = p_new.next

        p = head
        p_new = head_new
        while p is not None:
            if p.random is None:
                p_new.random = None
            else:
                p_new.random = node_id_dic[p.random]
            p = p.next
            p_new = p_new.next

        return head_new


if __name__ == '__main__':
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    node_copied = Solution().copyRandomList(node1)
    print(node_copied)
