from typing import Union

"""
bit 的下标是从 1 开始，总长度是 n + 1
如下实现里面的 i 表示的是从 1 开始的 index
tree[i] = sum([i - lowbit(i) + 1, i]
"""


class BinaryIndexedTree:
    def __init__(self, size):
        self._size = size
        self.tree = [0] * (self._size + 1)

    def lowbit(self, _x: int) -> int:
        return _x & (-_x)

    def query(self, i: int) -> Union[int, float]:
        # 查询 arr 的 i 及其之前的 sum
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res

    def update(self, i, delta) -> None:
        while i <= self._size:
            self.tree[i] += delta
            i += self.lowbit(i)

    def query_range(self, start, end) -> Union[int, float]:
        return self.query(end) - self.query(start - 1)


def test_binary_indexed_tree():
    # 初始化数组
    arr = [1, 2, 3, 4, 5]
    bit = BinaryIndexedTree(len(arr))

    # 构建 BIT
    for i, val in enumerate(arr):
        bit.update(i + 1, val)  # BIT 从 1 开始索引

    # 测试前缀和查询
    print("前缀和查询:")
    print(f"前 3 个元素的和: {bit.query(3)}")  # 1 + 2 + 3 = 6
    print(f"前 5 个元素的和: {bit.query(5)}")  # 1 + 2 + 3 + 4 + 5 = 15

    # 测试区间和查询
    print("\n区间和查询:")
    print(f"区间 [2, 4] 的和: {bit.query_range(2, 4)}")  # 2 + 3 + 4 = 9
    print(f"区间 [1, 5] 的和: {bit.query_range(1, 5)}")  # 1 + 2 + 3 + 4 + 5 = 15

    # 测试单点更新
    print("\n单点更新:")
    bit.update(3, 10)  # 将第 3 个元素从 3 改为 13（增加了 10）
    print(f"更新后前 3 个元素的和: {bit.query(3)}")  # 1 + 2 + 13 = 16
    print(f"更新后区间 [2, 4] 的和: {bit.query_range(2, 4)}")  # 2 + 13 + 4 = 19


if __name__ == "__main__":
    test_binary_indexed_tree()
