class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        T(n): O(n) # 这里的时间复杂度主要来自于删除 # 节点
        S(n): O(n)
        这里需要证明一个充要条件
            A: slot >= 0 和 B: 为前序空叶子树
            可以证明:
                1: B => A
                2: not B => not A(等价于 A => B)
        """
        slot = 1
        for item in preorder.split(','):
            slot -= 1
            if slot < 0:
                return False
            if item != '#':
                slot += 1
        return slot == 0


if __name__ == "__main__":
    s = Solution()
    # @formatter:off
    print(s.isValidSerialization("9,0,0,#,#,3,#,7,5,4,#,3,#,9,#,#,8,#,#,9,#,#,4,#,#,1,#,8,#,#,3,2,2,3,#,#,1,#,#,2,1,#,#,2,#,2,2,#,#,#,9,8,#"))
    # @formatter:on
