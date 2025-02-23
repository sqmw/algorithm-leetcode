import collections


class BIT:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)  # BIT 从 1 开始索引

    def lowbit(self, x):
        return x & (-x)  # 计算 lowbit

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta  # 更新当前节点
            i += self.lowbit(i)  # 跳到下一个节点

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]  # 累加当前节点
            i -= self.lowbit(i)  # 跳到上一个节点
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)  # 区间和查询


if __name__ == "__main__":

    print("1" > "2")
