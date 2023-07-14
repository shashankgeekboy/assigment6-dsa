def multiply_sparse_matrices(mat1, mat2):
  result = []

  for i in range(len(mat1)):
    row = []
    for j in range(len(mat2[0])):
      product = 0
      for k in range(len(mat2)):
        if mat1[i][k] != 0 and mat2[k][j] != 0:
          product += mat1[i][k] * mat2[k][j]
      row.append(product)
    result.append(row)

  return result


def main():
  mat1 = [[1,0,0],[-1,0,3]]
  mat2 = [[7,0,0],[0,0,0],[0,0,1]]

  result = multiply_sparse_matrices(mat1, mat2)
  print(result)


if __name__ == "__main__":
  main()
