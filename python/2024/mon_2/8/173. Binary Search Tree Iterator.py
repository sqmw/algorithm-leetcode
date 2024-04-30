# Definition for a binary tree node.
from python.util.core import tree_util


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorder_traverse(_root: TreeNode):
            nonlocal self
            if _root is not None:
                inorder_traverse(_root.left)
                self.node_list.append(_root)
                inorder_traverse(_root.right)

        self.node_list: List[TreeNode] = []
        self.now_index = -1
        inorder_traverse(root)

    def next(self) -> int:
        self.now_index += 1
        return self.node_list[self.now_index].val

    def hasNext(self) -> bool:
        if self.now_index >= len(self.node_list) - 1:
            return False
        return True


if __name__ == "__main__":
    null = None
    bst = BSTIterator(tree_util.list2tree_breadth_first_traverse([7, 3, 15, null, null, 9, 20]))
    print(bst.next())
    print(bst.next())
    print(bst.next())
    print(bst.next())
    print(bst.next())