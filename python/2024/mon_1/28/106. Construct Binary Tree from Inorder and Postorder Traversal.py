from typing import List, Optional

from python.util.core.tree_util import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        :param inorder: 中序遍历序列用来掌控位置的
        :param postorder:
        :return:
        """
        inorder_dic: dict = {}
        for i in range(len(inorder)):
            inorder_dic[inorder[i]] = i

        def is_left(_set_val, _root_val):
            return inorder_dic[_set_val] < inorder_dic[_root_val]

        postorder.reverse()
        root = TreeNode(postorder[0])

        def set_node(_root: TreeNode):
            nonlocal node
            if is_left(node.val, _root.val):
                if _root.left is None:
                    _root.left = node
                else:
                    set_node(_root.left)
            else:
                if _root.right is None:
                    _root.right = node
                else:
                    set_node(_root.right)

        for i in range(1, len(postorder)):
            node = TreeNode(postorder[i])
            # print(node.val)
            set_node(root)
        return root


if __name__ == "__main__":
    s = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    tree = s.buildTree(inorder, postorder)
    print(tree)
