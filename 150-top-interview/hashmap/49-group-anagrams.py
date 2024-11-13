'''
49. Group Anagrams
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        #! Brainchild
        # maps = []
        # result = []

        # for word in strs:
        #     word_map = {}
        #     for char in word:
        #         if char in word_map:
        #             word_map[char]+=1
        #         else:
        #             word_map[char] = 1
        #     if not maps:
        #         maps.append(word_map)
        #         result.append([word])
        #     else:
        #         if word_map not in maps:
        #             maps.append(word_map)
        #             result.append([word])
        #         else:
        #             result[maps.index(word_map)].append(word)

        # return result

        maps = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in maps:
                maps[key].append(word)
            else:
                maps[key] = [word]

        return list(maps.values())


def main():
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


if __name__ == '__main__':
    main()
