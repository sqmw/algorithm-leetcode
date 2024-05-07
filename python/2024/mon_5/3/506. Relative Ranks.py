from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        使用 heap 或者内置的排序算法, 这里不需要使用字典，字典耗性能
        T(n): O(nlog(n))
        S(n): O(n)
        """
        ini_val_index_tuple_list: List[tuple] = []
        for i in range(len(score)):
            # (score, score_index)
            ini_val_index_tuple_list.append((score[i], i))
        ini_val_index_tuple_list.sort(key=lambda t: t[0], reverse=True)
        medal: List[str] = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        # 定义目标返回值
        des_rank_list: List[str] = [''] * len(score)
        # print(ini_val_index_tuple_list)
        for i in range(min(3, len(des_rank_list))):
            t = ini_val_index_tuple_list[i]
            des_rank_list[t[1]] = medal[i]
        for i in range(3, len(ini_val_index_tuple_list)):
            t = ini_val_index_tuple_list[i]
            des_rank_list[t[1]] = f"{i + 1}"

        return des_rank_list


if __name__ == "__main__":
    s = Solution()
    print(s.findRelativeRanks([1]))
