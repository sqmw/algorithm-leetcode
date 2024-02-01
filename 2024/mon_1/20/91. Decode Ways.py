"""
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"


"11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)


使用traceback方法时间很长，很慢，不等你通过
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        使用回溯算法实现
        :param s:
        :return:
        """
        if len(s) == 0 or s[0] == '0' or s.find('00') != -1:
            return 0

        def traceback():
            nonlocal des_count
            nonlocal now_index
            if now_index > len(s) - 1:
                des_count += 1
                # print(path)
            else:
                # 仅仅是一位
                if now_index == len(s) - 1 or s[now_index + 1] != '0':
                    # path.append(s[now_index])
                    now_index += 1
                    traceback()
                    # path.pop()
                    now_index -= 1
                # 表示是两位
                if now_index < len(s) - 1:
                    if s[now_index + 1] == '0' or (
                            1 <= int(s[now_index]) * 10 + int(s[now_index + 1]) <= 26
                            and ((now_index == len(s) - 2) or (now_index + 2 < len(s) and s[now_index + 2] != '0'))):
                        # path.append(s[now_index: now_index + 2])
                        now_index += 2
                        traceback()
                        # path.pop()
                        now_index -= 2

        # path = []
        des_count = 0
        # 表示现在将要操作的字符的下标
        now_index = 0
        traceback()
        return des_count


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('"111111111111111111111111111111111111111111111"'))
