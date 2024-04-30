from typing import Set


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        """
        method1: 这里使用深度优先遍历进行搜索求得结果
        T(n): O(k * diff_change_methods)
        S(n): O(recurse_len)
        method2:
            因为变换在两个数字之间，那么必然是有相关的公式的，两个数字的差等的变化的范围在常数方范围内
        """
        if x + y < target:
            return False
        # 如果重合了，说明需要返回了
        x_y_capacity_set: Set[tuple] = set()
        can_reach: bool = False

        def depth_first_search(_x: int, _y: int):
            nonlocal can_reach
            nonlocal x_y_capacity_set
            if can_reach or (_x, _y) in x_y_capacity_set:
                return
            x_y_capacity_set.add((_x, _y))
            if _x + _y == target:
                can_reach = True

            _x_need = x - _x
            _y_need = y - _y
            # 这下面进行的是广度优先搜索
            # x -> y
            if _y_need < _x:
                depth_first_search(_x - _y_need, y)
            else:
                depth_first_search(0, _y + _x)
            # y -> x
            if _x_need < _y:
                depth_first_search(x, _y - _x_need)
            else:
                depth_first_search(_x + _y, 0)
            # _x 自填
            depth_first_search(x, _y)
            # _y 自填
            depth_first_search(_x, y)

            # _x 自空
            depth_first_search(0, _y)
            # _y 自空
            depth_first_search(_x, 0)

        depth_first_search(x, y)
        return can_reach


if __name__ == "__main__":
    s = Solution()
    print(s.canMeasureWater(3, 4, 5))
