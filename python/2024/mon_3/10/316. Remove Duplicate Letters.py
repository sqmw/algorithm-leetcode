import collections
import sys
from typing import Dict, List, Optional


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        method1:
            使用字典存储所有的 letter 的出现下标
                1. 按照 a-z 的顺序进行遍历字母，找到满足当下的字母能够按照序列出现的最小的 index: O(26)
                2. 在出现的 a-z 个字母里面，按照顺序，挑出第一个符合要求的，并且这个字母的下标必须大于上一 letter 的 index，被挑选的 letter 应该被删除: O(n)
                3. 挑完直到所有的字母都挑选了一遍
        这个方法可能是暴力解法，T(n) == O(k * n)
        T(n): O(n)
        S(n): O(n)下标
        """
        des_str = ''
        # k: letter(str)  v: letter_indexes(List)
        letter_dic: Dict[str, List] = collections.defaultdict(list)
        for i in range(len(s)):
            # 这里的 v 放进去之后就是有序的
            letter_dic[s[i]].append(i)
        letter_list: List[str] = list(letter_dic.keys())
        letter_list.sort()
        last_index = -1
        _min_letter: Optional[None | str] = None
        while len(letter_list) > 0:
            _min_index = sys.maxsize
            for k, v in letter_dic.items():
                if v[-1] < _min_index:
                    _min_index = v[-1]
                    _min_letter = k
            can_break = False
            for i in range(len(letter_list)):
                if can_break:
                    break
                for _index in letter_dic[letter_list[i]]:
                    if last_index < _index <= _min_index:
                        can_break = True
                        des_str += letter_list[i]
                        last_index = _index
                        del letter_dic[letter_list[i]]
                        del letter_list[i]
                        break

        # 'acdb'
        return des_str


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicateLetters('bcabc'))
