from typing import List


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        T,S 都不能通过
        0: 00   001 002 003 004 005
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
        41 42 43 44

        # 动态规划
        0 1 2 3 4 5 6 7 8 9
        10 ?? 12 13 14 15 16 17 18 19
        20 21 ?? 23 24 25 26 27 28 29
        30 31 32 ?? 34 35 36 37 38 39
        ...
        90 91 92 93 94 95 96 97 98 ??

        120 123 124 ...

        T(n): O(10 ** n)
        S(n): O(10 ** n)
        """

        def recurse_change(param: List[str]):
            """
            这里接收的 param 必须是 含有重复的有效数字
            只要找到一个，就会不断递归下去
            """
            nonlocal unique_list
            # 在各个位置依次插入 0,1,2,3,4,...
            now_num = int(''.join(param))
            # print(now_num)
            if now_num >= 10 ** n or visited[now_num] is True:
                return
            if now_num > 10 and len(param) <= n and visited[now_num] is False and \
                    not (now_num % 10 == 0 and now_num < 100):
                unique_list[now_num] = False
                # print(now_num)
            visited[now_num] = True
            for k in range(len(param) + 1):
                for j in range(10):
                    t_param = param[:]
                    t_param.insert(k, str(j))
                    recurse_change(t_param)

        _max_val = 10 ** n - 1
        # False: 表示不是 unique 的，也就是有重复的了
        unique_list: List[bool] = [True] * (10 ** n)
        visited: List[bool] = [False] * (10 ** n)
        for s_item in ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']:
            # 在原来的基础上面添加一位
            recurse_change(list(s_item))
        return sum(unique_list)


if __name__ == "__main__":
    s = Solution()
    print(s.countNumbersWithUniqueDigits(5))
