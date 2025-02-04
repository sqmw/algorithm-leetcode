from typing import List


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        T(n): O(n)
        S(n): O(n)
        """
        # 其实也可以不翻转的
        s = s.upper()
        _s_list: List[str] = []
        for char in s:
            if char != '-':
                _s_list.append(char)
        # 先翻转
        _s_list.reverse()
        # print(_s_list)

        _des_str_list: List[str] = []
        for i in range(0, len(_s_list), k):
            for j in range(min(k, len(_s_list) - i)):
                _des_str_list.append(_s_list[i + j])
            _des_str_list.append('-')
        if len(_des_str_list) > 0:
            _des_str_list.pop()
        _des_str_list.reverse()
        return ''.join(_des_str_list)


if __name__ == "__main__":
    s = Solution()
    print(s.licenseKeyFormatting(s="---", k=3))
