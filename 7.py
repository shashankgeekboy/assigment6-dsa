def spiral_matrix(n):
  matrix = [[0 for _ in range(n)] for _ in range(n)]
  row = 0
  col = 0
  num = 1

  while num <= n * n:
    for i in range(col, n):
      matrix[row][i] = num
      num += 1
    row += 1

    for i in range(row, n):
      matrix[i][n - 1] = num
      num += 1
    n -= 1

    if row > 0:
      for i in range(n - 1, col, -1):
        matrix[n - 1][i] = num
        num += 1
    col += 1

    if col < n:
      for i in range(n - 1, row, -1):
        matrix[i][col] = num
        num += 1
    row -= 1

  return matrix


def main():
  n = 3

  matrix = spiral_matrix(n)
  print(matrix)


if __name__ == "__main__":
  main()
