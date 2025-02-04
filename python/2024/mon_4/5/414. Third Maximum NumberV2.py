from typing import List

from sortedcontainers import SortedList


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        method2: 使用 SortedSet[也就是 SortedList]
        T(n): O(n)
        S(n): O(1)
        """
        sorted_list = SortedList()
        for num in nums:
            if num not in sorted_list:
                sorted_list.add(num)
                if len(sorted_list) > 3:
                    sorted_list.pop(0)
        return sorted_list[0] if len(sorted_list) == 3 else max(sorted_list)


if __name__ == "__main__":
    s = Solution()
    print(s.thirdMax([3, 1, 2, 2]))
