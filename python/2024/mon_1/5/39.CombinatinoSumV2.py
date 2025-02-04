from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        des_arr = []
        path = []
        self.traceback(0, candidates, des_arr, path, target)
        return des_arr

    def traceback(self, start: int, candidates, des_arr: List[List[int]], path: List[int], diff: int):
        if diff == 0:
            des_arr.append(path[:])
            return
        elif diff < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.traceback(i, candidates, des_arr, path, diff - candidates[i])
            path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([3, 5, 8, 9, 10, 11, 15, 21, 22, 25, 26, 27, 30, 32, 36], 39))
