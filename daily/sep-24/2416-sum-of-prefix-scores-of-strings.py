'''
2416. Sum of Prefix Scores of Strings
Solved
Hard
Topics
Companies
Hint
You are given an array words of size n consisting of non-empty strings.

We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.

 

Example 1:

Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
Explanation: The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.
Example 2:

Input: words = ["abcd"]
Output: [4]
Explanation:
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists of lowercase English letters.
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        # How many words pass through this node (i.e., how many have this prefix)
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Every time we visit a node, increment the count

    def prefix_score(self, word):
        node = self.root
        score = 0
        for char in word:
            node = node.children[char]
            score += node.count
        return score

    def visualize(self, node=None, level=0, prefix=""):
        if node is None:
            node = self.root

        for char, child in node.children.items():
            print(f"{' ' * level}- {prefix + char} (count: {child.count})")
            self.visualize(child, level + 2, prefix + char)


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()

        # Insert all the words into the Trie
        for word in words:
            trie.insert(word)

        # print("\nTrie Visualization:")
        # trie.visualize()

        # Calculate the sum of prefix scores for each word
        result = []
        for word in words:
            result.append(trie.prefix_score(word))

        return result


def main():
    words = ["abc", "ab", "bc", "b"]
    print(Solution().sumPrefixScores(words))  # Output: [5, 4, 3, 2]


if __name__ == '__main__':
    main()
