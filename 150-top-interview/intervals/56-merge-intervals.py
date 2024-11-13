'''
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.

 
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort()
        result = [intervals[0]]
        current_end_time = result[0][1]

        for start, end in intervals[1:]:
            if start <= current_end_time:
                current_end_time = max(current_end_time, end)
                result[-1][1] = current_end_time
            else:
                current_end_time = end
                result.append([start, end])

        return result


def main():
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # Expected output: [[1,6],[8,10],[15,18]]


if __name__ == '__main__':
    main()
