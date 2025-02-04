from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        T(n): O(n)
        S(n): O(n) # 这里的 T(n) 来自对数据的二进制转化，但是是非必要的，可以直接对原数组进行扫描判断, 此时 T(n): O(1)
        """
        _bin_str_list: List[str] = []
        # 处理 data 为二进制
        for num in data:
            _bin_str_list.append(bin(num)[2:][-8::].zfill(8))
        i = 0
        # 每次都扫描查找
        while i < len(_bin_str_list):
            # 表示是一字节的
            if _bin_str_list[i].startswith('0'):
                i += 1
                continue
            # 两字节的
            elif _bin_str_list[i].startswith('110'):
                for j in range(1, 2):
                    if i + j >= len(_bin_str_list) or not _bin_str_list[i + j].startswith('10'):
                        return False
                i += 2
            # 三字节的
            elif _bin_str_list[i].startswith('1110'):
                for j in range(1, 3):
                    if i + j >= len(_bin_str_list) or not _bin_str_list[i + j].startswith('10'):
                        return False
                i += 3
            # 四字节的
            elif _bin_str_list[i].startswith('11110'):
                for j in range(1, 4):
                    if i + j >= len(_bin_str_list) or not _bin_str_list[i + j].startswith('10'):
                        return False
                i += 4
            else:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.validUtf8([240, 162, 138, 147]))
