'''
241. Different Ways to Add Parentheses
Solved
Medium
Topics
Companies
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
'''


class Solution:
    memo = {}

    def diffWaysToCompute(self, expr: str) -> list[int]:
        if expr in self.memo:
            return self.memo[expr]

        result = []

        for i, char in enumerate(expr):
            if char in '+-*':
                '''If the current character is an operator Split the expression into left and right based on the 
                current operator. Recursively compute for the left  and right part'''
                left_results = self.diffWaysToCompute(expr[:i])
                right_results = self.diffWaysToCompute(expr[i+1:])

                # Combine the results from the left and right parts using the current operator
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            result.append(left + right)
                        elif char == '-':
                            result.append(left - right)
                        elif char == '*':
                            result.append(left * right)

        if not result:
            result.append(int(expr))

        self.memo[expr] = result
        return result


def main():
    solution = Solution()

    print(solution.diffWaysToCompute("2-1-1"))
    # Expected output: [0, 2]

    print(solution.diffWaysToCompute("2*3-4*5"))
    # Expected output: [-34, -14, -10, -10, 10]


if __name__ == '__main__':
    main()
