# Write a python script for palindrome checking without reversing the string.
def is_palindrome(text):
  text = text.lower()
  left = 0
  right = len(text) - 1
  while left < right:
    if text[left] != text[right]:
      return False
    left += 1
    right -= 1
  return True

text1 = input("enter a string: ")
if text1 == text1[::-1]:
  print(f"'{text1}' is a palindrome")
else:
  print(f"'{text1}' is not a palindrome")

