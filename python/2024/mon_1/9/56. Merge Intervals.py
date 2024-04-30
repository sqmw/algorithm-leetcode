from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda t: t[0])
        start = intervals[0][0]
        stop = intervals[0][1]
        des_arr: List[List[int]] = []
        for i in range(1, len(intervals)):
            if start <= intervals[i][0] <= stop or start <= intervals[i][1] <= stop:
                stop = max(intervals[i][1], stop)
            else:
                des_arr.append([start, stop])
                start = intervals[i][0]
                stop = intervals[i][1]
        des_arr.append([start, stop])
        return des_arr


if __name__ == '__main__':
    s = Solution()
    a = [[1, 3], [2, 6], [8, 10], [15, 18]]
    a.sort(key=lambda t: t[0])
    print(s.merge(a))
