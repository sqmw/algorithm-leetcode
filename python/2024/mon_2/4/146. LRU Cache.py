import collections
from typing import List, Dict


class LRUCache:
    """
    这道题使用C语言实现更有意义
    时间复杂度太高
        - 仔细发现，时间复杂度高的原因来自 对 _queue 的维护，因为 List 底层使用数组实现，因此效率很低，
        - 如果需要降低时间复杂度，唯一的办法就是使用 链表 ... C ... 想到了吧
    """

    def __init__(self, capacity: int):
        # 使用对立来维护 LRU 的先后顺序
        self._queue: List[int] = []
        self._capacity = capacity
        self._kv_dic: Dict[int, int] = {}
        # dict 用来检索 _queue 里面的数据，长度和 _queue 的一样们，k 为 _queue 里面的值，v 对应为 index

    def get(self, key: int) -> int:
        if key in self._queue:
            self._queue.remove(key)
            self._queue.insert(0, key)
            return self._kv_dic.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._queue:
            self._queue.remove(value)
            self._queue.insert(0, value)
        else:
            if len(self._queue) == self._capacity:
                # del 的时间时间复杂度 O(capacity)
                del self._kv_dic[self._queue.pop()]
            self._queue.insert(0, value)
            self._kv_dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    lruCache = LRUCache(2)
    """
    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]
    """
    print(lruCache.put(1, 1))
    print(lruCache.put(2, 2))
    print(lruCache.get(1))
    print(lruCache.put(3, 3))
    print(lruCache.get(2))
    print(lruCache.put(4, 4))
    print(lruCache.get(1))
    print(lruCache.get(3))
    print(lruCache.get(4))
