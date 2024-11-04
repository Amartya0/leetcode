'''
2530. Maximal Score After Applying K Operations
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

 

Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.
 

Constraints:

1 <= nums.length, k <= 105
1 <= nums[i] <= 109
'''

# import math

# class maxHeap:
#     def __init__(self):
#         self.heap = []

#     def parent(self, index):
#         return (index - 1)//2

#     def leftChild(self, index):
#         return 2 * index + 1

#     def rightChild(self, index):
#         return 2 * index + 2

#     def swap(self, findex, sindex):
#         self.heap[findex], self.heap[sindex] = self.heap[sindex], self.heap[findex]

#     def heapifyDown(self, index):
#         largest = index
#         left = self.leftChild(index)
#         right = self.rightChild(index)

#         if left < len(self.heap) and self.heap[left] > self.heap[largest]:
#             largest = left

#         if right < len(self.heap) and self.heap[right] > self.heap[largest]:
#             largest = right

#         if largest != index:
#             self.swap(largest, index)
#             self.heapifyDown(largest)

#     def customExtract(self):
#         if len(self.heap) == 0:
#             return None
#         elif len(self.heap) == 1:
#             root = self.heap[0]
#             self.heap[0] = math.ceil(root/3)
#             return root
#         else:
#             root = self.heap[0]
#             self.heap[0] = math.ceil(root/3)
#             self.heapifyDown(0)
#             return root


#     def buildHeap(self, arr):
#         self.heap = arr
#         for i in range((len(self.heap) // 2) - 1, -1, -1):
#             self.heapifyDown(i)

# class Solution:
#     def maxKelements(self, nums: List[int], k: int) -> int:
#         max_heap = maxHeap()
#         max_heap.buildHeap(nums)
#         result = 0
#         for _ in range(k):
#             result+= max_heap.customExtract()

#         return result

import heapq
import math


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        result = 0

        for _ in range(k):
            value = - heapq.heappop(max_heap)
            result += value
            heapq.heappush(max_heap, - math.ceil(value/3))

        return result


def main():
    print(Solution().maxKelements([1, 10, 3, 3, 3], 3))  # 17


if __name__ == '__main__':
    main()
