from typing import List, Dict


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        numerator_is_positive = 1
        denominator_is_positive = 1
        if numerator < 0:
            numerator_is_positive = -1
            numerator = -numerator
        if denominator < 0:
            denominator_is_positive = -1
            denominator = -denominator
        des_list: List[str] = []
        dot_added = False
        if numerator >= denominator:
            des_list.append(str(numerator // denominator))
            numerator %= denominator
        else:
            des_list.append('0')
        recur_dic: Dict[tuple, int] = {}
        while numerator != 0:
            if (numerator, denominator) in recur_dic:
                # print(recur_dic[(numerator, denominator)])
                des_list.insert(recur_dic[(numerator, denominator)], '(')
                des_list.append(')')
                break
            recur_dic[(numerator, denominator)] = len(des_list)
            if numerator // denominator == 0:
                if dot_added:
                    des_list.append('0')
                    numerator *= 10
                else:
                    des_list.append('')
                    numerator *= 10
                    dot_added = True
            else:
                des_list.append(str(numerator // denominator))
                numerator = 10 * (numerator % denominator)
        if numerator_is_positive * denominator_is_positive < 0:
            return '-' + ''.join(des_list)
        else:
            return ''.join(des_list)


if __name__ == "__main__":
    print(Solution().fractionToDecimal(-2, -2111111))
