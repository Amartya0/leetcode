'''
386. Lexicographical Numbers
Solved
Medium
Topics
Companies
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
'''


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        temp = 1
        for _ in range(n):
            res.append(temp)
            if temp*10 <= n:
                temp *= 10
            else:
                if temp >= n:
                    temp //= 10
                temp += 1
                while temp % 10 == 0:
                    temp //= 10

        return res


def main():
    print(Solution().lexicalOrder(13))  # [1,10,11,12,13,2,3,4,5,6,7,8,9]


if __name__ == '__main__':
    main()
