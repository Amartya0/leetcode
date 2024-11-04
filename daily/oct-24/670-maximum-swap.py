'''
670. Maximum Swap
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(map(int, str(num)))
        s_digits = sorted(digits, reverse=True)
        n = len(digits)
        start_index = 0

        while digits[start_index] == s_digits[start_index] and start_index < n - 1:
            start_index += 1

        if start_index == n - 1:
            return num

        swap_index = start_index
        max = digits[swap_index]

        for i in range(start_index, n):
            if digits[i] >= max:
                max = digits[i]
                swap_index = i

        if swap_index == start_index:
            return num
        else:
            digits[swap_index], digits[start_index] = digits[start_index], digits[swap_index]
            return int(''.join(str(i) for i in digits))


def main():
    print(Solution().maximumSwap(2736))  # 7236


if __name__ == '__main__':
    main()
