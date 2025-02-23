class BIT:
    def __init__(self, size: int):
        self._size = size
        self.tree = [0]*(size + 1)

    def query(self, i: int) -> int | float:
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self._lowbit(i)
        return res

    def _lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, i: int, delta: int | float) -> None:
        while i <= self._size:
            self.tree[i] += delta
            i += self._lowbit(i)



