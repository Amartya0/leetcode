'''
729. My Calendar I
Solved
Medium
Topics
Companies
Hint
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
'''

import bisect


class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_left(self.bookings, (start, end))
        if i > 0 and self.bookings[i - 1][1] > start:
            return False
        if i < len(self.bookings) and self.bookings[i][0] < end:
            return False

        self.bookings.insert(i, (start, end))
        return True


def main():
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))
    # returns True, no overlap

    print(myCalendar.book(50, 60))
    # returns True, no overlap

    print(myCalendar.book(10, 40))
    # returns False, overlapping with [10, 20]

    print(myCalendar.book(5, 15))
    # returns False, overlapping with [10, 20]

    print(myCalendar.book(5, 10))
    # returns True, no overlap

    print(myCalendar.book(25, 55))
    # returns False, overlapping with [50, 60]


if __name__ == '__main__':
    main()
