from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # print(candidates)
        des_arr = []
        path = []

        def traceback(start, diff):
            if diff == 0:
                des_arr.append(path[:])
                return
            elif diff < 0:
                return
            i = start + 1
            candidate = candidates[0] - 1
            while i < len(candidates):
                if candidates[i] != candidate:
                    candidate = candidates[i]
                    path.append(candidates[i])
                    traceback(i, diff - candidates[i])
                    path.pop()
                i += 1

        traceback(- 1, target)
        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 30))
