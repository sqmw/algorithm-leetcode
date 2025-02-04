from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 假设单词的长度都是相同的
        des_str_list_arr: List[List[str]] = []
        strs.sort(key=lambda s1: sorted(list(s1)))
        last_diff = '0'
        str_list: List[str] = []
        for item in strs:
            if sorted(list(item)) == sorted(list(last_diff)):
                str_list.append(item)
            else:
                if last_diff != '0':
                    des_str_list_arr.append(str_list)
                str_list = [item]
                last_diff = item
        des_str_list_arr.append(str_list)
        return des_str_list_arr


if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))
    print(strs)
