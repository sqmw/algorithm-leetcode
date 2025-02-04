from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        des_arr: List[List[int]] = []
        if newInterval[0] <= intervals[0][0] and intervals[len(intervals) - 1][1] <= newInterval[1]:
            return [newInterval]
        # newInterval 在最左边
        if newInterval[1] < intervals[0][0]:
            des_arr.append(newInterval)
            for i in range(len(intervals)):
                des_arr.append(intervals[i])
            return des_arr
        # newInterval 在最右边
        elif intervals[len(intervals) - 1][1] < newInterval[0]:
            des_arr = intervals[:]
            des_arr.append(newInterval)
            return des_arr
        # newInterval 在中间
        else:
            # start == -1 : newInterval[0] < intervals[0][0]
            # 其他类似类推
            start_index = stop_index = None
            start_in = True
            stop_in = True
            # 确定 start stop_index 的位置
            for i in range(len(intervals)):
                # 确定 start 的位置
                if start_index is None and newInterval[0] < intervals[i][0]:
                    if i == 0:
                        start_index = -1
                        start_in = False
                    elif newInterval[0] <= intervals[i - 1][1]:
                        start_index = i - 1
                    else:
                        start_index = i
                        start_in = False
                # 确定 stop_index 的位置
                if stop_index is None and intervals[i][1] > newInterval[1]:
                    if intervals[i][0] <= newInterval[1]:
                        stop_index = i
                    else:
                        stop_index = i
                        stop_in = False
            if stop_index is None:
                stop_index = len(intervals)
                stop_in = False
            if start_index is None:
                start_index = len(intervals) - 1
            # print(f'{start_index, start_in}, {stop_index, stop_in}')
            for i in range(0, start_index):
                des_arr.append(intervals[i])
            inserted_arr: List[int] = []
            if start_in:
                inserted_arr.append(min(newInterval[0], intervals[start_index][0]))
            else:
                inserted_arr.append(newInterval[0])
            if stop_in:
                inserted_arr.append(intervals[stop_index][1])
            else:
                inserted_arr.append(newInterval[1])
            des_arr.append(inserted_arr)
            if stop_in:
                for i in range(stop_index + 1, len(intervals)):
                    des_arr.append(intervals[i])
            else:
                for i in range(stop_index, len(intervals)):
                    des_arr.append(intervals[i])

        return des_arr


if __name__ == '__main__':
    s = Solution()  # [[1,2],[3,10],[12,16]]
    print(s.insert([[0, 2], [3, 3], [6, 11]], [9, 15]))
