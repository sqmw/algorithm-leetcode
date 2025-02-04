import collections
from typing import List, Dict


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        实际难度：中等
        T(n): O(n + m)
        S(n): O(n + m)
        """
        _next_bigger_val_dic: Dict[int, int] = collections.defaultdict(lambda: -1)
        # 用来存储还没有找到下一个更大的 _stack
        _stack: List[int] = []
        for i in range(len(nums2)):
            if len(_stack) == 0:
                _stack.append(nums2[i])
            else:
                if nums2[i] < _stack[-1]:
                    _stack.append(nums2[i])
                # nums2[i] > _stack[-1]
                else:
                    while len(_stack) > 0 and _stack[-1] < nums2[i]:
                        _popped = _stack.pop()
                        _next_bigger_val_dic[_popped] = nums2[i]
                    _stack.append(nums2[i])
        des_num: List[int] = []
        for num in nums1:
            des_num.append(_next_bigger_val_dic[num])
        return des_num


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [4, 3, 1, 2, 5]))
