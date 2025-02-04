import collections
from typing import Dict, Set


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        采用分治、hash、递归实现
        T(n): O(h*n) # h 表示的事递归树的高度
        S(n): O(h * 1) # 递归树的高度
        """

        # 使用分治思想
        # 两个都是包含
        # 如果 right 往前 能够让右边
        def find_max(_left: int, _right: int, _cou_dic: Dict[str, int]) -> int:
            # 找到其中一个在区间 [_left, _right] 不符合条件的，如果都符合，就返回现在的长度
            less_char_set: Set[str] = {char for char, cou in _cou_dic.items() if cou < k}
            if len(less_char_set) == 0:
                return _right - _left + 1
            start = _left
            _max_len = 0
            for i in range(_left, _right + 1):
                if s[i] in less_char_set:
                    _max_len = max(_max_len, find_max(start, i - 1, collections.Counter(s[start:i])))
                    start = i + 1
            # 加上末尾的一段
            _max_len = max(_max_len, find_max(start, _right, collections.Counter(s[start:_right + 1])))
            return _max_len

        return find_max(0, len(s) - 1, collections.Counter(s))


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubstring("bbaaace", 3))
