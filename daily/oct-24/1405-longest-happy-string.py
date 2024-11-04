'''
1405. Longest Happy String
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no 
such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        result = []

        while max_heap:
            count1, letter1 = heapq.heappop(max_heap)

            if len(result) >= 2 and result[-1] == result[-2] == letter1:
                if not max_heap:
                    break
                count2, letter2 = heapq.heappop(max_heap)
                result.append(letter2)
                count2 += 1
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, letter2))
                heapq.heappush(max_heap, (count1, letter1))
            else:
                result.append(letter1)
                count1 += 1
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, letter1))

        return ''.join(result)


def main():
    print(Solution().longestDiverseString(1, 1, 7))
    # Output: "ccaccbcc"
    print(Solution().longestDiverseString(7, 1, 0))
    # Output: "aabaa"
    print(Solution().longestDiverseString(7, 1, 1))
    # Output: "aabac"
    print(Solution().longestDiverseString(7, 7, 7))
    # Output: "abcabcabcabcabcabcabc"


if __name__ == '__main__':
    main()
