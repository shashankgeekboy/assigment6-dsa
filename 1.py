def reconstruct_permutation(s):
  permutation = []
  for i in range(len(s)):
    if s[i] == "I":
      permutation.append(i)
    else:
      permutation.append(len(s) - i - 1)

  return permutation


def main():
  s = "IDID"

  permutation = reconstruct_permutation(s)
  print(permutation)


if __name__ == "__main__":
  main()
