def max_len_subarray_with_equal_0_and_1(nums):
  count_0 = 0
  count_1 = 0
  max_len = 0

  for i in range(len(nums)):
    if nums[i] == 0:
      count_0 += 1
    else:
      count_1 += 1

    if count_0 == count_1:
      max_len = max(max_len, count_0 + count_1)
    elif count_0 > count_1:
      count_0 = 0
    else:
      count_1 = 0

  return max_len


def main():
  nums = [0,1]

  max_len = max_len_subarray_with_equal_0_and_1(nums)
  print(max_len)


if __name__ == "__main__":
  main()

