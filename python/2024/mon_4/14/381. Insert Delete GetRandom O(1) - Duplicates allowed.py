import collections
import random
from typing import Dict, List, Optional


class RandomizedCollection:

    def __init__(self):
        # 两个需要是同步的,dict[_val, _index_list]
        self._val_index_dic: Dict[int, List[int]] = collections.defaultdict(list)
        self._val_list = list()

    def insert(self, val: int) -> bool:
        # 允许重复，有没有都需要加入
        not_in = False
        if len(self._val_index_dic[val]) < 1:
            not_in = True
        self._val_index_dic[val].append(len(self._val_list))
        self._val_list.append(val)

        return not_in

    def remove(self, val: int) -> bool:
        """
        时间复杂度来自这里,但是实际上也是可以降低为 O(1) 的，下面使用排序，但是实际上将 dict[val, index_list]
        将其中的 index_list 换成 set 性能就能够提升了，就不会涉及到下面的排序
        """
        if len(self._val_index_dic[val]) < 1:
            return False
        # 在 dict 和 list 里面已经有了
        else:
            # 这里需要做的就是把它移动到末尾去，再弹出去
            if val != self._val_list[-1]:
                # 实现思路，将需要移除的通过交换数字，移动到末尾，此时就把时间复杂度降低到 O(1)
                inner_val_index = self._val_index_dic[val][-1]
                # 把末尾和内部那个交换
                self._val_list[inner_val_index] = self._val_list[-1]
                self._val_index_dic[self._val_list[inner_val_index]].pop()
                self._val_index_dic[self._val_list[inner_val_index]].append(inner_val_index)
                # 排了一下序，性能稍微差了点
                self._val_index_dic[self._val_list[inner_val_index]].sort()
                del self._val_index_dic[val][-1]
                self._val_list.pop()
            else:
                self._val_list.pop()
                self._val_index_dic[val].pop()
            return True

    def getRandom(self) -> int:
        return self._val_list[random.randint(0, len(self._val_list) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
if __name__ == "__main__":
    action_list = ["RandomizedCollection", "insert", "insert", "insert", "insert", "insert", "insert", "remove",
                   "remove", "remove", "remove", "remove", "insert", "remove", "remove", "getRandom", "getRandom",
                   "getRandom", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom",
                   "getRandom"]
    val_list = [[], [10], [10], [20], [20], [30], [30], [10], [20], [20], [10], [30], [40], [30], [30], [], [], [], [],
                [], [], [], [], [], []]
    r: Optional[RandomizedCollection] = None
    for i in range(len(action_list)):
        if i == 7:
            ...
        if action_list[i] == 'RandomizedCollection':
            r = RandomizedCollection()
        elif action_list[i] == 'insert':
            print(r.insert(val_list[i][0]))
        elif action_list[i] == 'remove':
            print(r.remove(val_list[i][0]))
        elif action_list[i] == 'getRandom':
            print(r.getRandom())
