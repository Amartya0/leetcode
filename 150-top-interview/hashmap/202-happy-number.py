'''
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does 
not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1

'''


class Solution:

    def sum_of_squares(self, n: int) -> int:
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += digit * digit
            n //= 10
        return total_sum

    def isHappy(self, n: int) -> bool:
        #! brainchild
        # forms = set()
        # while (n != 1):
        #     n = self.sum_of_squares(n)
        #     if n in forms:
        #         return False
        #     else:
        #         forms.add(n)
        # return True

        #! Floyd's Cycle Detection algorithm (also known as the "tortoise and hare" algorithm),
        #! which is commonly used to detect cycles in linked lists, to check for cycles without needing extra
        #! space for the set

        slow = n
        fast = self.sum_of_squares(n)
        while fast != 1 and slow != fast:
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(self.sum_of_squares(fast))
        return fast == 1


def main():
    print(Solution().isHappy(19))  # True
    print(Solution().isHappy(2))  # False


if __name__ == '__main__':
    main()
