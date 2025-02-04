import collections
from typing import List, Dict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        m == count(distinct num)
        T(n): O(max(mlog(m),n))
        S(n): O(count(distinct num))
        """
        num_cou_dic: Dict[int, int] = collections.defaultdict(lambda: 0)
        for num in nums:
            num_cou_dic[num] += 1

        tuple_list: List[tuple] = [(k, v) for k, v in num_cou_dic.items()]
        tuple_list.sort(reverse=True, key=lambda x: x[1])
        return [tuple_list[i][0] for i in range(k)]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([4, 4, 4, 4, 4, 2, 3, 3, 4, 5, 6, 7, 8, 1, 1, 5, 4, 4], 2))
