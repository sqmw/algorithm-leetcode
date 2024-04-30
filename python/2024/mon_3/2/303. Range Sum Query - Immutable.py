from typing import List


class NumArray:
    """
    T(n): O(1)
    S(n): O(n)
    """

    def __init__(self, nums: List[int]):
        # 表示的是当前及其前面的所有和
        self.sum_nums = []
        total: int = 0
        for item in nums:
            total += item
            self.sum_nums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        # 需要处理边界
        left = max(0, left)
        right = min(len(self.sum_nums) - 1, right)
        if left > 0:
            return self.sum_nums[right] - self.sum_nums[left - 1]
        else:
            return self.sum_nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    obj = NumArray([0, 1, 2, 3, 4, 5])
    print(obj.sumRange(1, 1))
