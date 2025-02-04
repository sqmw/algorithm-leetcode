from typing import List


class Solution:
    nums2letters_dic = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z'),
    }

    def carry(self, select_arr, map_arr, j):

        if select_arr[j] == len(map_arr[j]) - 1:
            select_arr[j] = 0
            if j > 0:
                # select_arr[j - 1] = (select_arr[j - 1] + 1) % len(map_arr[j - 1])
                self.carry(select_arr, map_arr, j - 1)
            else:
                return
        else:
            select_arr[j] = (select_arr[j] + 1) % len(map_arr[j])

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        map_arr = []
        des_list = []
        arr_len = 1
        for i in digits:
            map_arr.append(self.nums2letters_dic.get(i))
            arr_len *= len(self.nums2letters_dic.get(i))
        select = 0  # 表示轮到0号元组被挑选
        select_arr = []  # 表示对应的元组被挑选到哪一个了
        for i in range(0, len(digits)):
            select_arr.append(0)

        while len(des_list) < arr_len:
            tempStr = ''
            # 一个循环取出一次
            for i in range(0, len(digits)):
                tempStr += map_arr[select][select_arr[select]]
                # 元组里面的元素下一个
                # select_arr[select] = (select_arr[select] + 1) % len(map_arr[select])
                # 表示的是刚刚在最后的一个元组里面选了出来，还没有+1
                if select == len(select_arr) - 1:
                    # 递归函数
                    self.carry(select_arr, map_arr, select)
                # 换下一个元组来取
                select = (select + 1) % len(digits)
            des_list.append(tempStr)
        return des_list


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("232343432334"))
