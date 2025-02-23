from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
        使用选择排序
        T(n): O(n**4) => 超时
        S(n): O(1)
        """
        # i 之前都是已经排序无误的了
        for i in range(len(people)):
            # 选中 j 位置的放在 i 位置
            for j in range(i, len(people)):
                t_val = people[j][1]
                for k in range(i):
                    if people[k][0] >= people[j][0]:
                        t_val -= 1
                if t_val != 0:
                    continue
                have_err = False
                people[i], people[j] = people[j], people[i]
                for k in range(i + 1, len(people)):
                    t_val = people[k][1]
                    for q in range(i + 1):
                        if people[q][0] >= people[k][0]:
                            t_val -= 1
                    if t_val < 0:
                        have_err = True
                        break
                if have_err:
                    continue
                # people[i], people[j] = people[j], people[i]
                break
        return people


if __name__ == '__main__':
    s = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    # [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    print(s.reconstructQueue(people))
