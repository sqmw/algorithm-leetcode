from typing import List, Union


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        感觉和C语言的 string.h 里面的 compare 基本一致的
        :param version1:
        :param version2:
        :return:
        """
        version_list1: List[Union[int | str]] = version1.split('.')
        version_list2: List[int | str] = version2.split('.')
        for i in range(len(version_list1)):
            version_list1[i] = int(version_list1[i])
        for i in range(len(version_list2)):
            version_list2[i] = int(version_list2[i])
        same_len: int = min(len(version_list1), len(version_list2))
        for i in range(same_len):
            if version_list1[i] > version_list2[i]:
                return 1
            elif version_list1[i] < version_list2[i]:
                return -1
        for i in range(same_len, len(version_list1)):
            if version_list1[i] > 0:
                return 1

        for i in range(same_len, len(version_list2)):
            if version_list2[i] > 0:
                return -1

        return 0


if __name__ == "__main__":
    print(Solution().compareVersion(version1="0.1", version2="1.1"))
