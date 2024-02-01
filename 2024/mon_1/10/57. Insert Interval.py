from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        des_arr: List[List[int]] = []
        start = None
        end = None
        start_index: int = -1
        end_index = -1
        inserted = False
        for i in range(len(intervals)):
            # 前面插入
            if i == 0 and newInterval[1] < intervals[i][0]:
                des_arr.append(newInterval)
            # if intervals[i][0] <= newInterval[0] <= intervals[i][1] or \
            #         intervals[i][0] <= newInterval[1] <= intervals[i][1] or \
            #         (start is not None and (start <= intervals[i][0] <= end or start <= intervals[i][1] <= end)):
            if intervals[i][0] <= newInterval[0] <= intervals[i][1] or \
                    newInterval[0] < intervals[i][0] or \
                    (start is not None and (start <= intervals[i][0] <= end or start <= intervals[i][1] <= end)):
                if start_index == -1:
                    start = min(intervals[i][0], newInterval[0])
                    end = max(intervals[i][1], newInterval[1])
                    start_index = i
                    end_index = i
                else:
                    end = max(intervals[i][1], newInterval[1])
                    end_index = i
            else:
                if not inserted and start is not None:
                    inserted = True
                    des_arr.append([min(newInterval[0], intervals[start_index][0]),
                                    max(newInterval[1], intervals[end_index][1])])
                des_arr.append(intervals[i])
            # 这个表示没有交集以及末尾插入的情况
            if (intervals[i][1] < newInterval[0]) and (
                    i + 1 >= len(intervals) or newInterval[1] < intervals[i + 1][0]):
                start = min(intervals[i][0], newInterval[0])
                end = max(intervals[i][1], newInterval[1])
                start_index = i
                end_index = i
                des_arr.append(newInterval)

        if not inserted and start is not None:
            des_arr.append([min(newInterval[0], intervals[start_index][0]),
                            max(newInterval[1], intervals[end_index][1])])
        return des_arr


if __name__ == '__main__':
    s = Solution()  # [[1,2],[3,10],[12,16]]
    print(s.insert([[-2, -1], [1, 2], [7, 9]], [0, 6]))
