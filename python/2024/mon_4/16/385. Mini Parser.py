# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        """
        首先需要实现的是字符串的解析
            1. 得到一个新的 str_list
            2. 使用栈对 str_list 进行解析
            3. 解析得到 Python 的基本数据类型
            4. 将基本的 Python 的数据类型封装成题目给的类型，得到结果(其实就是把自己转化好的 int 或者 list 直接在外面套一个 NestedInteger 就可以了)

            T(n): O(n)
            S(n): O(n)
        """
        s_list: List[str] = []
        # 处理切割字符串于 List[str] 里面
        i = 0
        while i < len(s):
            # 表示非数字
            if s[i] == '[' or s[i] == ']' or s[i] == ',':
                s_list.append(s[i])
                i += 1
            elif s[i] == ' ':
                i += 1
            # 表示数字
            else:
                # s[i] 可能是符号位
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                s_list.append(s[i: j])
                i = j
        if s_list[0] != '[':
            return NestedInteger(int(s_list[0]))
        print(s_list)

        def recurse_get_py_list(now_index: int) -> tuple[List, int]:
            """
            这里使用递归实现了 list_int_str 的 JSON 解析
            :param now_index:
            :return:
            """
            now_arr: List[int | List] = []
            i = now_index
            while i < len(s_list):
                if s_list[i] == '[':
                    next_arr, bracket_index = recurse_get_py_list(i + 1)
                    now_arr.append(next_arr)
                    i = bracket_index + 1
                elif s_list[i] == ']':
                    return now_arr, i
                elif s_list[i] == ',':
                    i += 1
                # elif s_list[i].isdigit():
                # '-1'.isdigit() : False
                # 这里表示是数字的时候
                else:
                    now_arr.append(int(s_list[i]))
                    i += 1
            return now_arr, i

        # 对于解析得到的 py_obj 进行按照题目转化
        des_py_list, _ = recurse_get_py_list(1)
        print(des_py_list)

        return NestedInteger(des_py_list)


if __name__ == "__main__":
    s = Solution()
    print(s.deserialize("[-1]"))
