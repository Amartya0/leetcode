class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        # optimized two-pointer approach
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped

        # n = len(height)
        # left = [0]*n
        # right = [0]*n
        # left[0] = height[0]
        # right[n-1] = height[n-1]
        # water_trapped = 0

        # for i in range(1, n):
        #     left[i] = max(left[i-1], height[i])
        # for i in range(n-2, -1, -1):
        #     right[i] = max(right[i+1], height[i])
        #     water_trapped += min(left[i], right[i])-height[i]

        # return water_trapped


def main():
    height_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
    height_2 = [4, 2, 0, 3, 2, 5]  # 9
    print(Solution().trap(height_1))
    print(Solution().trap(height_2))


if __name__ == '__main__':
    main()
