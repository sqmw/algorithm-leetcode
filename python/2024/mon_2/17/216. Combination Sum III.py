from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def traceback(start_val: int):
            if len(path) == k and sum(path) == n:
                des_nums_list.append(path[:])
            elif len(path) > k or sum(path) == n:
                return
            else:
                for i in range(start_val, 10):
                    path.append(i)
                    traceback(i + 1)
                    path.pop()

        des_nums_list: List[List[int]] = []
        path: List[int] = []

        traceback(1)

        return des_nums_list


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 7))
