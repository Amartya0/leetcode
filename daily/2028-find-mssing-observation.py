'''
05/09/2024
2028. Find Missing Observations
Solved
Medium
Topics
Companies
Hint
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

 

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
Example 3:

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
 

Constraints:

m == rolls.length
1 <= n, m <= 105
1 <= rolls[i], mean <= 6
'''


def missingRolls(rolls, mean, n):
    '''
    #ChatGPT
    m = len(rolls)
    total_sum = mean * (n + m)
    observed_sum = sum(rolls)

    missing_sum = total_sum - observed_sum
    if missing_sum < n or missing_sum > 6 * n:
        return []

    result = [1] * n
    remaining_sum = missing_sum - n
    for i in range(n):
        add_value = min(remaining_sum, 5)
        result[i] += add_value
        remaining_sum -= add_value
        if remaining_sum == 0:
            break

    return result
    '''

    sum_of_missing = mean*(len(rolls)+n) - sum(rolls)
    result = []
    i = 0
    if (sum_of_missing < n or sum_of_missing > 6*n):
        return []
    while (sum_of_missing - 6 >= n-i-1):
        result.append(6)
        sum_of_missing -= 6
        i += 1
    if (i < n-1 and sum_of_missing < n-i-1 and i > 0):
        sum_of_missing += 6
        result[i-1] = 1
    while (i < n-1):
        result.append(1)
        sum_of_missing -= 1
        i += 1
    if (sum_of_missing != 0):
        result.append(sum_of_missing)
    return result


def main():
    rolls = [1, 5, 6]
    mean = 3
    n = 4
    print(missingRolls(rolls, mean, n))


if __name__ == '__main__':
    main()
