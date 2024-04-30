import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self._init_nums = nums

    def reset(self) -> List[int]:
        # T(n): O(1)
        # S(n): O(1)
        return self._init_nums

    def shuffle(self) -> List[int]:
        """
        这里需要模拟洗牌，
        下面实现了一个洗牌算法
        """
        copped_nums = self._init_nums.copy()
        # 使用下面的这个方法来 shuffle，如果仅仅操作其中的一半的话，打乱不够充分
        # for i in range(len(copped_nums) // 2 + 1):
        for i in range(len(copped_nums)):
            gap = random.randint(0, len(copped_nums) - 1)
            swap_index = (gap + i) % len(copped_nums)
            copped_nums[i], copped_nums[swap_index] = copped_nums[swap_index], copped_nums[i]
        return copped_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


if __name__ == "__main__":
    s = Solution([0, 1, 2, 3, 4])
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
