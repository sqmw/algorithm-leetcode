import json
from math import ceil, sqrt
from typing import Optional


class NumArray:
    """
    T(n): O((operation_cou // 100) * num_len)
    S(n): O(num_len)
    这里只是一个大概得值
    我这里的方法把更新过程延迟到 100 次修改之后，但是每次的求和都需要 O(100) 的次数来进行遍历字典
    总结： 显然，通过调节 延迟次数 可以调节时间，此时显然不均匀的，如何才能得到一个最好延迟数量呢？
    """

    def __init__(self, nums):
        """
        按照V2的性能性能提升方法，这里将会合理进行分段
        每一段数据量为 n**0.5，分段的数量为 n**0.5
        加入数据有 10 个，每一组为 seg_num_cou: int(10**0.5) == 3 个，总共为 seg_cou: ceil(10 / 3) 组
        每一组的和放在[0-2,3-5,6-8,9-9]里面(对应为 index // seg_num_cou)
        """
        self.n = len(nums)  # 数组的总长度
        self.nums = nums[:]  # 复制数组以便更新
        self.block_size = int(ceil(sqrt(self.n)))  # 每块的大小为根号n
        self.blocks = [0] * self.block_size  # 初始化每个块的和为0
        for i in range(self.n):  # 填充每个块的和
            self.blocks[i // self.block_size] += self.nums[i]

    def update(self, index, val):
        block_index = index // self.block_size  # 找到所在块的索引
        self.blocks[block_index] += val - self.nums[index]  # 更新块的和
        self.nums[index] = val  # 更新原数组

    def sumRange(self, left, right):
        sum = 0
        start_block = left // self.block_size  # 起始块的索引
        end_block = right // self.block_size  # 结束块的索引
        if start_block == end_block:  # 如果在同一个块中
            for i in range(left, right + 1):
                sum += self.nums[i]
        else:
            # 跨越多个块
            for i in range(left, (start_block + 1) * self.block_size):
                sum += self.nums[i]  # 加上起始块中的剩余元素
            for i in range(start_block + 1, end_block):
                sum += self.blocks[i]  # 加上完整块的和
            for i in range(end_block * self.block_size, right + 1):
                sum += self.nums[i]  # 加上结束块中的元素
        return sum


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
