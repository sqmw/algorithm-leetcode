from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Example 1:
        Input: s = "25525511135"
        Output: ["255.255.11.135","255.255.111.35"]

        Example 2:
        Input: s = "0000"
        Output: ["0.0.0.0"]

        Example 3:
        Input: s = "101023"
        Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
        :param s:
        :return:
        """

        def is_between(_s: str) -> bool:
            if len(_s)>1 and _s[0] == '0':
                return False
            if 0 <= int(_s) <= 255:
                return True
            return False

        def traceback():
            nonlocal now_index
            if len(path) == 4:
                if now_index == len(s):
                    des_arr.append('.'.join(path))
            elif len(path) > 4:
                return
            else:  # 0 <= path.len <= 3
                for i in range(1, 4):
                    if now_index + i <= len(s) and is_between(s[now_index: now_index + i]):
                        path.append(s[now_index: now_index + i])
                        now_index += i
                        traceback()
                        now_index -= i
                        path.pop()

        now_index = 0
        des_arr: List[str] = []
        path: List[str] = []
        traceback()
        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses('0000'))  # ["255.255.11.135","255.255.111.35"]
