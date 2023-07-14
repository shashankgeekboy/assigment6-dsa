def is_mountain_array(arr):
  if len(arr) < 3:
    return False

  increasing = True
  for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
      increasing = False
    elif not increasing and arr[i] <= arr[i - 1]:
      return False

  return increasing


def main():
  arr = [2, 1]

  is_mountain_array = is_mountain_array(arr)
  print(is_mountain_array)


if __name__ == "__main__":
  main()
