from typing import List


class NumArray:
    """
    T(n): O(n)
    S(n): O(n)
    超时
    """

    def __init__(self, nums: List[int]):
        self._sum_arr = []
        _total = 0
        for item in nums:
            _total += item
            self._sum_arr.append(_total)

    def update(self, index: int, val: int) -> None:
        diff: int = ((self._sum_arr[index - 1] if index > 0 else 0) + val) - self._sum_arr[index]
        for i in range(index, len(self._sum_arr)):
            self._sum_arr[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        return self._sum_arr[right] - (self._sum_arr[left - 1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == "__main__":
    numArr = NumArray([1, 3, 5])
    print(numArr.sumRange(0, 2))
    numArr.update(1, 2)
    print(numArr.sumRange(0, 2))
