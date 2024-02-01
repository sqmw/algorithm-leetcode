from typing import List
"""
这个方法是枚举法，时间上通过不了
"""
"""
经过优化，已经能够通过，非递归实现
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        des_arr = []
        candidates_tuple = []
        i = 0
        while i < len(candidates):
            temp = int(target / candidates[i])
            if temp < 1:
                candidates.remove(candidates[i])
                continue
            candidates_tuple.append([candidates[i], temp])
            i += 1
        select_arr = [0 for _ in range(0, len(candidates))]
        canOver = False
        while not canOver:
            end_not_index = len(select_arr) - 1
            candidates_sum = self._sum(candidates, select_arr)
            if candidates_sum == target:
                temp_arr = []
                for i in range(0, len(select_arr)):
                    for times in range(0, select_arr[i]):
                        temp_arr.append(candidates[i])
                des_arr.append(temp_arr)
                # print(" == ", select_arr)
            elif candidates_sum > target:
                end_not_index = -1
                for i in range(len(select_arr) - 1, -1, -1):
                    if select_arr[i] != 0:
                        end_not_index = i
                        break
                # print(">", select_arr)
            _ = 0
            for i in range(end_not_index, -1, -1):
                _ += (select_arr[i] - candidates_tuple[i][1])
            if _ == 0:
                canOver = True
                # print(select_arr, candidates_tuple)
            carry = 1
            for i in range(end_not_index, -1, -1):
                if select_arr[i] + carry == candidates_tuple[i][1] + 1:
                    select_arr[i] = 0
                    carry = 1
                else:
                    select_arr[i] += 1
                    break
        return des_arr

    def _sum(self, candidates, select_arr) -> int:
        total = 0
        for i in range(0, len(select_arr)):
            total += candidates[i] * select_arr[i]
        return total


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 7, 8], 6))
