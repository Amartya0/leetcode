def removeDuplicates(nums):
    array_length = len(nums)
    if array_length < 3:
        return array_length

    valid_count = 2
    temp_2 = nums[0]
    temp_1 = nums[1]
    valid_index = []
    valid_index.append(0)
    valid_index.append(1)

    for i in range(2, array_length):
        if nums[i] != temp_1 or nums[i] != temp_2:
            valid_index.append(i)
            valid_count += 1
            temp_1 = nums[i]
            temp_2 = nums[i-1]

    for i in range(valid_count):
        nums[i] = nums[valid_index[i]]

    return valid_count


def main():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3, 3]
    k = removeDuplicates(nums)
    print(nums[:k])


if __name__ == "__main__":
    main()
