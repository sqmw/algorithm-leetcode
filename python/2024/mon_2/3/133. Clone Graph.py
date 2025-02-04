# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional, List


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        按照题目意思就是手动实现一个图的复制
        :param node:
        :return:
        """
        if node is None:
            return None

        def recurse_copy(_node: Optional[Node], _now_need_set_neighbors: Optional[List[Node]]):
            if _node in finished:
                return
            else:
                for i in range(len(_node.neighbors)):
                    if _node.neighbors[i].val in node_dic:
                        _now_need_set_neighbors.append(node_dic.get(_node.neighbors[i].val))
                    else:
                        new_node = Node(_node.neighbors[i].val)
                        node_dic[_node.neighbors[i].val] = new_node
                        _now_need_set_neighbors.append(new_node)
                finished[_node] = True

                for i in range(len(_node.neighbors)):
                    if _node.neighbors[i] not in finished:
                        _now_need_set_neighbors[i].neighbors = []
                        recurse_copy(_node.neighbors[i], _now_need_set_neighbors[i].neighbors)

        # 将孩子设置好了的放在这里
        finished: dict[Node, bool] = {}
        node_dic: dict[int: Node] = {}
        start_node = Node(node.val)
        node_dic[node.val] = start_node
        start_node.neighbors = []

        recurse_copy(node, start_node.neighbors)
        return start_node


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    _copy = Solution().cloneGraph(node1)
    ...
