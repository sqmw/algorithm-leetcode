import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self._init_nums_tuple = tuple(nums)

    def reset(self) -> List[int]:
        return list(self._init_nums_tuple)

    def shuffle(self) -> List[int]:
        """
        这里需要模拟洗牌
        """
        index_arr = random.sample([i for i in range(len(self._init_nums_tuple))], len(self._init_nums_tuple))
        return [self._init_nums_tuple[index] for index in index_arr]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


if __name__ == "__main__":
    s = Solution([0, 1, 2, 3, 4])
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
