from typing import List


def sum_of_modes(arr: List[int]):
    count_1 = [0] * (len(arr) + 1)
    count_2 = [0] * (len(arr) + 1)

    for i in range(1, len(arr) + 1):
        count_1[i] = count_1[i - 1] + (1 if arr[i - 1] == 1 else 0)
        count_2[i] = count_2[i - 1] + (1 if arr[i - 1] == 2 else 0)

    sum_modes = 0
    for start in range(len(arr)):
        for end in range(start + 1, len(arr) + 1):
            ones = count_1[end] - count_1[start]
            twos = count_2[end] - count_2[start]
            if ones >= twos:
                sum_modes += 1
            else:
                sum_modes += 2

    return sum_modes


if __name__ == "__main__":
    # Example usage:
    arr = [2, 1, 2]
    print(sum_of_modes(arr))
