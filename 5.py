def min_product_sum(nums1, nums2):
  sum1 = 0
  sum2 = 0

  for i in range(len(nums1)):
    sum1 += nums1[i]
    sum2 += nums2[i] * nums1[i]

  min_product_sum = sum1 * sum2

  for i in range(len(nums1)):
    temp = sum1 - nums1[i]
    min_product_sum = min(min_product_sum, temp * sum2 + nums1[i] * sum2)

  return min_product_sum


def main():
  nums1 = [5,3,4,2]
  nums2 = [4,2,2,5]

  min_product_sum = min_product_sum(nums1, nums2)
  print(min_product_sum)


if __name__ == "__main__":
  main()
