import string
if __name__ == '__main__':
  letters = list(string.ascii_lowercase)
  nums = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
  for n in nums:
    print(letters[n-1])
