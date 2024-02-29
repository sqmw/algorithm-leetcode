from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        T(n): O(n * n)
        S(n): O(1)
        :param gas:
        :param cost:
        :return:
        """
        index = - 1
        same_len = len(gas)
        # 表示起点
        for i in range(0, same_len):
            car_gas = gas[i]
            # 前往下一个车站，最后回到自己
            for j in range(1, same_len + 1):
                car_gas -= cost[(i + j - 1) % same_len]
                if car_gas < 0:
                    break
                else:
                    car_gas += gas[(i + j) % same_len]
            if car_gas >= 0:
                index = i
                break

        return index


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    print(Solution().canCompleteCircuit(gas, cost))
