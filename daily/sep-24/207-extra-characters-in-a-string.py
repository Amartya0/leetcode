'''
2707. Extra Characters in a String
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words
'''

#! Dynamic Programming Approach with naive inner loop
# class Solution:
#     def minExtraChar(self, s: str, dictionary: list[str]) -> int:
#         word_set = set(dictionary)
#         n = len(s)
#         dp = [n+1] * (n + 1)
#         dp[0] = 0
#         for i in range(1, n + 1):
#             for j in range(i):
#                 if s[j:i] in word_set:
#                     dp[i] = min(dp[i], dp[j])
#                 else:
#                     dp[i] = min(dp[i], dp[j] + (i - j))
#         return dp[n]

#! Dynamic Programming Approach with optimized inner loop


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        word_set = set(dictionary)
        longest_word = max(len(word) for word in dictionary)
        n = len(s)
        # Create a dp array where dp[i] represents the minimum number of extra characters
        # needed to match the first i characters of string s.
        # Initialize it with a large number, since we want to minimize the value.
        dp = [n + 1] * (n + 1)
        dp[0] = 0  # Base case: No characters mean 0 extra characters.

        # Iterate over each possible endpoint i of a substring in the string s.
        for i in range(1, n + 1):
            # Inner loop checks all possible start points j for substrings ending at i.
            # Initially, this loop was written as `for j in range(0, i)`, meaning it considered
            # every possible substring from index 0 to i, making it O(n^2).

            # Optimization: We restrict the inner loop to only consider substrings within the
            # range `i - longest_word` to `i`. This is because any substring longer than the
            # longest word in the dictionary cannot be valid.
            for j in range(max(0, i - longest_word), i):
                # If the substring s[j:i] exists in the dictionary, then update dp[i] to reflect
                # the minimum extra characters needed. No extra characters if this substring matches.
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
                else:
                    # Otherwise, count the extra characters (i - j) as extra characters, and
                    # update dp[i] accordingly.
                    dp[i] = min(dp[i], dp[j] + (i - j))

        # Return the minimum extra characters needed to match the entire string s.
        return dp[n]


def main():
    s = "leetcoder"
    dictionary = ["leet", "code", "leetcode"]
    print(Solution().minExtraChar(s, dictionary))  # Expected output 1


if __name__ == '__main__':
    main()
