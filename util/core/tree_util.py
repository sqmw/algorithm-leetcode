from typing import List, Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2list_pre_traverse(tree: TreeNode) -> List:
    des_arr = []

    def pre_traverse(_tree: TreeNode):
        if _tree is not None:
            des_arr.append(_tree.val)
            pre_traverse(_tree.left)
            pre_traverse(_tree.right)
        else:
            des_arr.append(None)

    pre_traverse(tree)
    return des_arr


def list2tree_breadth_first_traverse(arr: List) -> Optional[TreeNode]:
    """
    通过深度优先遍历实现将数组转化为 Tree
    :param arr:
    :return:
    """
    if arr is None or len(arr) == 0:
        return None
    if len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    _queue = [root]
    index_arr = 1
    while index_arr < len(arr):
        _root = _queue.pop(0)
        if _root:
            if arr[index_arr] is not None:
                _root.left = TreeNode(arr[index_arr])
            else:
                _root.left = None
            _queue.append(_root.left)
            index_arr += 1
            if index_arr == len(arr):
                break
            if arr[index_arr] is not None:
                _root.right = TreeNode(arr[index_arr])
            else:
                _root.right = None
            _queue.append(_root.right)
            index_arr += 1
    return root


def is_bst2list(root: TreeNode) -> List:
    """
    :param root:
    :return: 返回 [] 表示树为空或者该树不是二叉搜索树，否则返回对应的数组
    """
    if root is None:
        return []
    visited_node: List[TreeNode] = []

    tree_nodes: List[TreeNode] = [root]
    value_list: List[int] = []
    _root = root

    while len(tree_nodes) > 0:
        # 左孩子
        if _root.left is not None and _root.left not in visited_node:
            tree_nodes.append(_root.left)
        # 右孩子
        else:
            visited_node.append(_root)
            value_list.append(_root.val)
            tree_nodes.pop()

            if _root.right is not None:
                if _root.right not in visited_node:
                    tree_nodes.append(_root.right)
        if len(tree_nodes) > 0:
            _root = tree_nodes[len(tree_nodes) - 1]
    for i in range(1, len(value_list)):
        if value_list[i - 1] >= value_list[i]:
            return []
    return value_list
