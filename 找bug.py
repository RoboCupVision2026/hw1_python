if __name__ == '__main__':
    nums = list(range(1000))
    for idx in range(len(nums)-1,-1,-1):
        if nums[idx] % 2 == 1:
            nums.pop(idx)
    print(nums)