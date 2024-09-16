'''
539. Minimum Time Difference
Solved
Medium
Topics
Companies
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
'''


class Solution:

    def timeToMin(self, time: str) -> int:
        hour, min = map(int, time.split(':'))
        return hour*60 + min

    def findMinDifference(self, timePoints: list[str]) -> int:
        timePointsInMin = [self.timeToMin(time) for time in timePoints]
        timePointsInMin.sort()
        minDiff = timePointsInMin[0]+24*60-timePointsInMin[-1]

        for i in range(1, len(timePointsInMin)):
            minDiff = min(minDiff, timePointsInMin[i]-timePointsInMin[i-1])

        return minDiff


def main():
    timePoints = ["00:00", "23:59", "00:00"]  # expected: 0
    print(Solution().findMinDifference(timePoints))

    timePoints = ["23:59", "00:00"]  # expected: 1
    print(Solution().findMinDifference(timePoints))

    timePoints = ["12:12", "00:13", "3:59", "00:00"]  # expected: 13
    print(Solution().findMinDifference(timePoints))


if __name__ == '__main__':
    main()
