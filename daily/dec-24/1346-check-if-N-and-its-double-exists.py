'''
1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 
Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:
2 <= arr.length <= 500
-103 <= arr[i] <= 103
'''


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        dp = set()

        for num in arr:
            if num*2 in dp:
                return True
            if num % 2 == 0 and num//2 in dp:
                return True
            dp.add(num)

        return False


def main():
    print(Solution().checkIfExist([10, 2, 5, 3]))  # True
    print(Solution().checkIfExist([3, 1, 7, 11]))  # False


if __name__ == '__main__':
    main()
