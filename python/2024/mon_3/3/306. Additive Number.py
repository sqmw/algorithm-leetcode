from typing import List


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        method1：使用回溯法，目前就是最优解
        T(n): O(n**3)
        S(n): O(n)
        难点：边界值的确定繁杂
        """
        is_additive: bool = False
        # path 表示的事每一个数字的结尾
        path: List[int] = [-1]

        def traceback():
            nonlocal is_additive
            nonlocal path
            if is_additive is True:
                return
            if len(path) >= 3:
                # i 表示的是arr[:i]是不包含的
                for i in range(path[-1] + 2, len(num) + 1):
                    if int(num[path[-1] + 1: i]) == \
                            int(num[path[-3] + 1: path[-2] + 1]) + int(num[path[-2] + 1: path[-1] + 1]) and \
                            not (num[path[-1] + 1] == '0' and i - 1 > path[-1] + 1):
                        if i == len(num):
                            is_additive = True
                            return
                        path.append(i - 1)
                        traceback()
                        path.pop()
            # 表示现在 num_cou < 2
            else:
                for i in range(path[-1] + 1, len(num)):
                    if num[path[-1] + 1] == '0' and i > path[-1] + 1:
                        continue
                    path.append(i)
                    traceback()
                    path.pop()

        traceback()
        return is_additive


if __name__ == "__main__":
    s = Solution()
    print(s.isAdditiveNumber("000"))
