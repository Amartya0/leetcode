'''
30. Substring with Concatenation of All Words
Solved
Hard
Topics
Companies
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
'''


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        words_count = {}
        for word in words:
            if word not in words_count:
                words_count[word] = 1
            else:
                words_count[word] += 1
        result = []

        # Iterate over all possible starting points
        for i in range(word_len):
            left = i
            right = i
            current_count = {}

            while right + word_len <= len(s):
                # Get the next word from the right side of the window
                word = s[right:right + word_len]
                right += word_len

                # If the word is in words_count, add it to the current window count
                if word in words_count:
                    if word not in current_count:
                        current_count[word] = 1
                    else:
                        current_count[word] += 1

                    # If the word occurs more times than it is in words_count, shrink the window
                    while current_count[word] > words_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len

                    # If the current window size matches total_len, record the start index
                    if right - left == total_len:
                        result.append(left)
                else:

                    current_count.clear()
                    left = right
                if left + total_len > len(s):
                    break

        return result


def main():
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(Solution().findSubstring(s, words))


if __name__ == '__main__':
    main()
