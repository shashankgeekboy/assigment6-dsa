def find_target(matrix, target):
  row = 0
  col = len(matrix[0]) - 1

  while row < len(matrix) and col >= 0:
    if matrix[row][col] == target:
      return True
    elif matrix[row][col] < target:
      row += 1
    else:
      col -= 1

  return False


def main():
  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
  target = 3

  is_found = find_target(matrix, target)
  print(is_found)


if __name__ == "__main__":
  main()
