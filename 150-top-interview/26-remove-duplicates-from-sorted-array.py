def removeDuplicates(nums):
    valid_count = 1
    array_length = len(nums)
    temp = nums[0]
    valid_index = []
    valid_index.append(0)
    for i in range(1, array_length):
        if nums[i] != temp:
            valid_index.append(i)
            valid_count += 1
            temp = nums[i]

    for i in range(valid_count):
        nums[i] = nums[valid_index[i]]

    return valid_count


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = removeDuplicates(nums)
    print(nums[:k])


if __name__ == "__main__":
    main()
