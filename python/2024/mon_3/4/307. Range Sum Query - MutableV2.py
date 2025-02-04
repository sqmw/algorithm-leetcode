import collections
import json
import sys
from typing import List, Dict, Optional


class NumArray:
    """
    T(n): O((operation_cou // 100) * num_len)
    S(n): O(num_len)
    这里只是一个大概得值
    我这里的方法把更新过程延迟到 100 次修改之后，但是每次的求和都需要 O(100) 的次数来进行遍历字典
    总结： 显然，通过调节 延迟次数 可以调节时间，此时显然不均匀的，如何才能得到一个最好延迟数量呢？
    """

    def __init__(self, nums: List[int]):
        self._init_nums = nums[:]
        self._sum_arr = []
        self._change_dic: Dict = collections.defaultdict(lambda: 0)
        self._index_min = sys.maxsize
        _total = 0
        for item in nums:
            _total += item
            self._sum_arr.append(_total)

    def update(self, index: int, val: int) -> None:
        # dict 有了 100 个之后再统一进行更新，否则时间复杂度很高
        self._index_min = min(self._index_min, index)
        self._change_dic[index] = val
        if len(self._change_dic) > 100:
            # 更新数组值
            for k, v in self._change_dic.items():
                self._init_nums[k] = v
            # 重新计算 _sum_arr
            # print(self._index_min)
            for i in range(self._index_min, len(self._init_nums)):
                self._sum_arr[i] = (self._sum_arr[i - 1] if i > 0 else 0) + self._init_nums[i]
            self._index_min = sys.maxsize
            self._change_dic: Dict = collections.defaultdict(lambda: 0)

    def sumRange(self, left: int, right: int) -> int:
        _val_change: int = 0
        for index in self._change_dic.keys():
            if left <= index <= right:
                _val_change += (self._change_dic[index] - self._init_nums[index])
        return self._sum_arr[right] - (self._sum_arr[left - 1] if left > 0 else 0) + _val_change


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == "__main__":
    with open('test_data.json') as file:
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
