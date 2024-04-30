from typing import List


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        a,#,#构成一个节点，删除 #,#,将 a 变成 #
        n: 表示包含 # 在内的节点的数量
        T(n): O(nlog(n)) # 这里的时间复杂度主要来自于删除 # 节点(这里应该使用栈实现才行...无语有大意了)
        S(n): O(n)
        """
        preorder_list: List[str] = preorder.split(',')
        try:
            i = 0
            while i < len(preorder_list) - 2 and len(preorder_list) > 1:
                if preorder_list[i].isdigit() and preorder_list[i + 1] == '#' and preorder_list[i + 2] == '#':
                    preorder_list[i] = '#'
                    del preorder_list[i + 1]
                    del preorder_list[i + 1]
                    if preorder_list[i - 1] == '#':
                        i -= 2
                    else:
                        i -= 1
                else:
                    i += 1
                if len(preorder_list) > 1 and preorder_list[0] == '#':
                    return False
        except IndexError as e:
            return False

        return len(preorder_list) == 1 and preorder_list[0] == '#'


if __name__ == "__main__":
    s = Solution()
    # @formatter:off
    print(s.isValidSerialization("9,0,0,#,#,3,#,7,5,4,#,3,#,9,#,#,8,#,#,9,#,#,4,#,#,1,#,8,#,#,3,2,2,3,#,#,1,#,#,2,1,#,#,2,#,2,2,#,#,#,9,8,#"))
    # @formatter:on
