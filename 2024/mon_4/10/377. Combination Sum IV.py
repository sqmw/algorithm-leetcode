from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        这里属于排列，需要考虑顺序的
        1: 1
        2: 1,1   2
        3: 1,1,1   2,1   1,2  3
        4: 1,1,1,1
        method1: 回溯枚举
            T(n): O(n**k) # 超时
            S(n): (k) # 表示的是地柜深度
        """
        path: List[int] = []
        diff_set: List[tuple] = []

        def traceback(_need: int) -> None:
            nonlocal diff_set, path
            if _need < 0:
                return
            elif _need == 0:
                _path_tuple = tuple(path)
                if _path_tuple not in diff_set:
                    diff_set.append(_path_tuple)
                return
            for i in range(len(nums)):
                path.append(nums[i])
                traceback(_need - nums[i])
                path.pop()

        traceback(target)
        print(diff_set)

        return len(diff_set)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum4([1, 2, 4], 8))
