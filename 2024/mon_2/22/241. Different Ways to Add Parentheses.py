#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Set


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        通过构造不同的表达式 tree 实现
        T(n): O(cou(operator) * h)
        S(n): O(1)
        """
        expression_list: List[int | str] = []
        i = 0
        operator_set: Set = {'+', '-', '*'}
        # 将字符串的表达式转化成 list 类型
        while i < len(expression):
            if expression[i] in operator_set:
                expression_list.append(expression[i])
                i += 1
            else:
                if i + 1 < len(expression) and expression[i + 1].isdigit():
                    expression_list.append(int(expression[i: i + 2]))
                    i += 2
                else:
                    expression_list.append(int(expression[i: i + 1]))
                    i += 1
        print(expression_list)

        # 通过后序遍历构造树，并且得到结果
        def postorder_traverse(start_index: int, operator_index: int, end_index: int):

            ...

        ...


if __name__ == "__main__":
    s = Solution()
    print(s.diffWaysToCompute('3+3+2*30-4*50'))
