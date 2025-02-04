import collections
import random
from typing import Dict, Optional, Set


class RandomizedCollection:
    """
    这里将会使用 set 来实现，时间复杂度将会降低到最低
    T(n): O(1)
    S(n): O(1)
    """

    def __init__(self):
        # 两个需要是同步的,dict[_val, _index_list]
        self._val_index_dic: Dict[int, Set[int]] = collections.defaultdict(set)
        self._val_list = list()

    def insert(self, val: int) -> bool:
        # 允许重复，有没有都需要加入
        not_in = False
        if len(self._val_index_dic[val]) < 1:
            not_in = True
        self._val_index_dic[val].add(len(self._val_list))
        self._val_list.append(val)

        return not_in

    def remove(self, val: int) -> bool:
        """
        时间复杂度来自这里,但是实际上也是可以降低为 O(1) 的，下面使用排序，但是实际上将 dict[val, index_list]
        将其中的 index_list 换成 set 性能就能够提升了，就不会涉及到下面的排序
        """
        if len(self._val_index_dic[val]) < 1:
            return False
        # 在 dict 和 set 里面已经有了
        else:
            # 这里需要做的就是把它移动到末尾去，再弹出去，这里有点像指针的那点，比较烦
            # 这里已经将时间复杂度降低到 O(1) 了
            # 具体的思路/操作：
            # 1. 找到需要 移除的val的 val_need_remove_index_set，然后弹出一个用来移除
            # 2. 将弹出来的那个 index 的值和最后一个值进行交换
            # 3. 修改set，在 list_last_val_set 里面弹出最后一个 index，添加之前需要弹出的 index
            # 4. list 弹出最后一个元素
            last_index_set = self._val_index_dic[self._val_list[-1]]
            inner_need_remove_index_set = self._val_index_dic[val]
            popped_index = inner_need_remove_index_set.pop()
            self._val_list[popped_index] = self._val_list[-1]
            last_index_set.add(popped_index)
            last_index_set.remove(len(self._val_list) - 1)
            self._val_list.pop()
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
        if action_list[i] == 'RandomizedCollection':
            r = RandomizedCollection()
        elif action_list[i] == 'insert':
            print(r.insert(val_list[i][0]))
        elif action_list[i] == 'remove':
            print(r.remove(val_list[i][0]))
        elif action_list[i] == 'getRandom':
            print(r.getRandom())
