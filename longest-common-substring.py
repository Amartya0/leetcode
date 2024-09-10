# naive algorithm
# Worst case Time complexity: O(m^3*n); where m is the length of shortest string and n is the number of strings

class naive_longest_common_substring:
    def longest_common_substring(self, strings):
        if not strings:
            return ""

        # Start with the first string as the initial common substring
        longest_substr = ""
        first_string = strings[0]

        for i in range(len(first_string)):
            for j in range(i + 1, len(first_string) + 1):
                substring = first_string[i:j]
                if all(substring in s for s in strings):
                    if len(substring) > len(longest_substr):
                        longest_substr = substring

        return longest_substr


# optimized using binary search and hashing
# Worst case Time complexity O(m*n*log(m)); where m is the length of shortest string and n is the number of strings

# class optimized_longest_common_substring:
#     def has_common_substring(self, strings, length):
#         # Use a set to store hashes of substrings of the first string
#         hashes = set()
#         first_string = strings[0]
#         base, mod = 256, 2**61 - 1

#         # Compute the hash of the first 'length' characters of the first string
#         hash_val = 0
#         for i in range(length):
#             hash_val = (hash_val * base + ord(first_string[i])) % mod
#         hashes.add(hash_val)

#         # Rolling hash for the remaining substrings in the first string
#         power = pow(base, length - 1, mod)
#         for i in range(1, len(first_string) - length + 1):
#             hash_val = (
#                 hash_val * base - ord(first_string[i - 1]) * power + ord(first_string[i + length - 1])) % mod
#             hashes.add(hash_val)

#         # Now check other strings for common substring of this length
#         for string in strings[1:]:
#             hash_val = 0
#             found = False
#             for i in range(length):
#                 hash_val = (hash_val * base + ord(string[i])) % mod
#             if hash_val in hashes:
#                 found = True

#             for i in range(1, len(string) - length + 1):
#                 hash_val = (
#                     hash_val * base - ord(string[i - 1]) * power + ord(string[i + length - 1])) % mod
#                 if hash_val in hashes:
#                     found = True
#                     break

#             if not found:
#                 return False

#         return True

#     def longest_common_substring(self, strings):
#         if not strings:
#             return ""

#         # Binary search on the length of the common substring
#         low, high = 0, min(len(s) for s in strings)
#         longest_substr_length = 0

#         while low <= high:
#             mid = (low + high) // 2
#             if self.has_common_substring(strings, mid):
#                 longest_substr_length = mid
#                 low = mid + 1
#             else:
#                 high = mid - 1

#         # Extract the longest common substring
#         for i in range(len(strings[0]) - longest_substr_length + 1):
#             candidate = strings[0][i:i + longest_substr_length]
#             if all(candidate in s for s in strings):
#                 return candidate

#         return ""


# Example usage
strings = ["interspace", "interstellar", "semi-interstate"]
result = naive_longest_common_substring().longest_common_substring(strings)
# result = optimized_longest_common_substring().longest_common_substring(strings)
print("Longest common substring:", result)
