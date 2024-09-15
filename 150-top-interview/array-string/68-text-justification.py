'''
68. Text Justification
Solved
Hard
Topics
Companies
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
'''


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        #! Brain child
        # # Initialize the length of words list and the current index for processing words
        # total_words = len(words)
        # current_word_index = 0

        # # Initialize variables to keep track of the current row of words and row length
        # current_row = []
        # current_row_length = 0
        # result_rows = []  # Stores all rows of words (before adjusting spaces)

        # # Iterate through the words list
        # while current_word_index < total_words:
        #     # Case 1: Adding a word without exceeding maxWidth (includes a space after the word)
        #     if current_row_length + len(words[current_word_index]) < maxWidth:
        #         current_row.append(words[current_word_index])
        #         # Add word length + 1 for space
        #         current_row_length += len(words[current_word_index]) + 1
        #         current_word_index += 1
        #     # Case 2: Adding a word exactly matches maxWidth (no need to add a space after it)
        #     elif current_row_length + len(words[current_word_index]) == maxWidth:
        #         current_row.append(words[current_word_index])
        #         # Only add the word length
        #         current_row_length += len(words[current_word_index])
        #         current_word_index += 1
        #     # Case 3: Row exceeds maxWidth, finalize the current row and start a new one
        #     else:
        #         # Save the row for space adjustment later
        #         result_rows.append(current_row)
        #         current_row_length = 0  # Reset the row length for the next row
        #         current_row = []  # Start a new row

        # # Final list that will store the fully justified lines
        # justified_text = []

        # # Process each row (except the last row) and adjust spaces
        # for row in result_rows:
        #     # If the row has only one word, left justify it by adding spaces to the right
        #     if len(row) == 1:
        #         justified_text.append(row[0] + ' ' * (maxWidth - len(row[0])))
        #     else:
        #         # Calculate total word lengths in the row
        #         total_word_lengths = sum(len(word) for word in row)
        #         # Total number of spaces to distribute
        #         total_spaces = maxWidth - total_word_lengths
        #         # Even spaces between words
        #         even_spaces = total_spaces // (len(row) - 1)
        #         # Extra spaces to distribute evenly
        #         extra_spaces = total_spaces % (len(row) - 1)

        #         temp_line = ''
        #         # Build the row with adjusted spaces
        #         for i in range(len(row) - 1):  # Iterate through all but the last word
        #             # Add even spaces between words
        #             temp_line += row[i] + ' ' * even_spaces
        #             if extra_spaces:  # Add one extra space if needed
        #                 temp_line += ' '
        #                 extra_spaces -= 1
        #         # Add the last word without extra spaces after it
        #         temp_line += row[-1]
        #         justified_text.append(temp_line)

        # # Special handling for the last row (left justify, no extra spaces between words)
        # temp_last_row = ''
        # for word in current_row:
        #     if word == current_row[-1]:
        #         # Add the last word and pad with spaces to the right
        #         temp_last_row += word + ' ' * \
        #             (maxWidth - len(temp_last_row) - len(word))
        #     else:
        #         # Add the word followed by a space
        #         temp_last_row += word + ' '
        # justified_text.append(temp_last_row)

        # return justified_text

        #! Brain child but in one loop
        # # Initialize necessary variables
        # total_words = len(words)  # Total number of words to process
        # current_word_index = 0  # Index to track the current word in the list
        # words_in_row = 0  # Count of words in the current row
        # # Tracks the length of the current row (including spaces)
        # current_row_length = 0
        # # Total length of words in the current row (without spaces)
        # total_words_length = 0
        # current_row = []  # List to hold words in the current row
        # temp_line = ''  # Temporary string to construct the row with appropriate spaces
        # justified_text = []  # Final result list to store fully justified lines

        # # Process all words in the list
        # while current_word_index < total_words:
        #     # Case 1: Adding the current word to the row does not exceed maxWidth (includes a space)
        #     if current_row_length + len(words[current_word_index]) < maxWidth:
        #         current_row.append(words[current_word_index])
        #         words_in_row += 1
        #         total_words_length += len(words[current_word_index])
        #         # Add space after the word
        #         current_row_length += len(words[current_word_index]) + 1
        #         current_word_index += 1
        #     # Case 2: Adding the current word exactly matches maxWidth
        #     elif current_row_length + len(words[current_word_index]) == maxWidth:
        #         current_row.append(words[current_word_index])
        #         words_in_row += 1
        #         total_words_length += len(words[current_word_index])
        #         # No extra space needed
        #         current_row_length += len(words[current_word_index])
        #         current_word_index += 1
        #     # Case 3: Current row is full, finalize the row and start a new one
        #     else:
        #         # If only one word in the row, left-justify the row by adding spaces at the end
        #         if words_in_row == 1:
        #             justified_text.append(
        #                 current_row[0] + ' ' * (maxWidth - total_words_length))
        #         else:
        #             # Distribute spaces evenly between words
        #             total_spaces = maxWidth - total_words_length
        #             # Minimum spaces between words
        #             even_spaces = total_spaces // (words_in_row - 1)
        #             # Extra spaces to distribute
        #             extra_spaces = total_spaces % (words_in_row - 1)

        #             # Construct the line by adding words and spaces
        #             for j in range(words_in_row - 1):
        #                 temp_line += current_row[j] + ' ' * even_spaces
        #                 if extra_spaces:  # Add one more space for words getting extra spaces
        #                     temp_line += ' '
        #                     extra_spaces -= 1
        #             # Add the last word without extra spaces after it
        #             temp_line += current_row[-1]

        #             # Add the justified line to the final result
        #             justified_text.append(temp_line)

        #         # Reset variables for the next row
        #         words_in_row = 0
        #         total_words_length = 0
        #         current_row_length = 0
        #         current_row = []
        #         temp_line = ''

        # # Handle the last row (left-justify, no extra spaces between words)
        # temp_line = ''
        # for word in current_row:
        #     if word == current_row[-1]:
        #         # Add the last word and pad the line with spaces on the right
        #         temp_line += word + ' ' * \
        #             (maxWidth - len(temp_line) - len(word))
        #     else:
        #         # Add word followed by a space
        #         temp_line += word + ' '
        # justified_text.append(temp_line)

        # return justified_text

        #! chatGpt solution
        res = []  # Final result list
        cur_line = []  # Current line to store words
        cur_length = 0  # Current line length (without spaces)

        for word in words:
            # Check if adding the next word would exceed the maxWidth
            if cur_length + len(cur_line) + len(word) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - cur_length):
                    # Add spaces between words, more spaces to the left slots
                    cur_line[i % (len(cur_line) - 1 or 1)] += ' '

                # Join current line to form justified line and add to result
                res.append(''.join(cur_line))
                cur_line, cur_length = [], 0  # Reset for the next line

            # Add the word to the current line
            cur_line.append(word)
            cur_length += len(word)

        # Last line (left-justified)
        res.append(' '.join(cur_line).ljust(maxWidth))

        return res


def main():
    sol = Solution()
    print(sol.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(sol.fullJustify(["What", "must", "be",
          "acknowledgment", "shall", "be"], 16))
    print(sol.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to",
          "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))


if __name__ == '__main__':
    main()
