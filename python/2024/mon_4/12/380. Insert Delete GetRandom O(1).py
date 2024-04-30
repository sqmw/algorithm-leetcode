import random


class RandomizedSet:
    """
    method1:
        整体而言性能符合题目的要求，但是应该是还可以提升的
    method2:
        使用一个 hash_map 来记录 val_index 这样 remove 的时间复杂度就可以降低到 O(1) 而不是 O(n)

    """

    def __init__(self):
        # 两个需要是同步的
        self._val_set = set()
        self._val_list = list()

    def insert(self, val: int) -> bool:
        if val not in self._val_set:
            self._val_set.add(val)
            self._val_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        时间复杂度来自这里
        """
        if val not in self._val_set:
            return False
        else:
            self._val_set.discard(val)
            self._val_list.remove(val)
            return True

    def getRandom(self) -> int:
        return self._val_list[random.randint(0, len(self._val_list) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
