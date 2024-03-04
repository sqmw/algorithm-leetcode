import json
from typing import List, Optional


class BIT:
    def __init__(self, n: int):
        self.sums = [0] * (n + 1)

    def update(self, i: int, delta: int):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & -i

    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= i & -i
        return s


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = BIT(len(nums))
        for i, num in enumerate(nums):
            self.tree.update(i + 1, num)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self.tree.update(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right + 1) - self.tree.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == "__main__":
    with open('./test_data.json') as file:
        test_data = json.loads(file.read())
    numArr: Optional[NumArray | None] = None

    cou = 0

    for _i in range(len(test_data['actions'])):
        if test_data['actions'][_i] == 'NumArray':
            numArr = NumArray(test_data['input'][_i][0])
        elif test_data['actions'][_i] == 'update':
            numArr.update(*test_data['input'][_i])
        elif test_data['actions'][_i] == 'sumRange':
            # print(numArr.sumRange(*test_data['input'][i]), test_data['output'][i])
            assert numArr.sumRange(*test_data['input'][_i]) == test_data['output'][_i]
