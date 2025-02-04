from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        通过回溯法实现
        """
        des_str_list: List[List[str]] = []
        is_palindrome_dic: dict[int:bool] = {}

        def is_palindrome(start_index, end):
            """
            [start, end)
            :param start_index:
            :param end:
            :return:
            """
            k = (start_index * 10 + end)
            if k in is_palindrome_dic:
                return is_palindrome_dic[k]
            else:
                for i in range(0, int((end - start_index) / 2)):
                    if s[start_index + i] != s[end - 1 - i]:
                        is_palindrome_dic[k] = False
                        return False
            return True

        path: List[str] = []
        now_len = 0

        def traceback():
            nonlocal now_len
            if now_len == len(s):
                des_str_list.append(path[:])
            else:
                # i 表示右边需要多少
                for i in range(1, len(s) - now_len + 1):
                    if is_palindrome(now_len, now_len + i):
                        # 这里直接切割申请字符串是不合理的，因为很多不合条件，应该放在判定当前的path已经可以组成一个s的时候
                        # 经过测试，这样的效率，挺高的
                        path.append(s[now_len: now_len + i])
                        now_len += i
                        traceback()
                        now_len -= i
                        path.pop()

        traceback()
        return des_str_list


if __name__ == "__main__":
    print(Solution().partition("aab"))
