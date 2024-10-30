'''
1813. Sentence Similarity III

You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a 
single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that 
the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

For example,

s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" 
by a space.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

 

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"

Output: false

Explanation:

No single sentence can be inserted inside one of the sentences to make it equal to the other.

Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

 

Constraints:

1 <= sentence1.length, sentence2.length <= 100
sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
The words in sentence1 and sentence2 are separated by a single space.
'''


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Store the smaller sentence in sentence2
        if len(sentence2) > len(sentence1):
            sentence1, sentence2 = sentence2, sentence1

        s1_words = list(map(str, sentence1.split(" ")))
        s2_words = list(map(str, sentence2.split(" ")))

        prefix_len = 0
        suffix_len = 0

        while (prefix_len < len(s2_words)) and s1_words[prefix_len] == s2_words[prefix_len]:
            prefix_len += 1

        while (suffix_len < len(s2_words) - prefix_len) and s1_words[-(suffix_len+1)] == s2_words[-(suffix_len+1)]:
            suffix_len += 1

        if prefix_len + suffix_len == len(s2_words):
            return True
        else:
            return False


def main():
    s = Solution()
    print(s.areSentencesSimilar("A B C D B B", "A B B"))  # True
    print(s.areSentencesSimilar("My name is Haley", "My Haley"))  # True


if __name__ == '__main__':
    main()
