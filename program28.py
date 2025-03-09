# Write a program to do basic set operations
def set_operations():
  set1 = set(input("Enter elements for set 1 (comma-separated): ").split(','))
  set2 = set(input("Enter elements for set 2 (comma-separated): ").split(','))

  print("\nSet 1:", set1)
  print("Set 2:", set2)

  print("\nUnion:", set1 | set2)
  print("Intersection:", set1 & set2)
  print("Difference (Set 1 - Set 2):", set1 - set2)
  print("Difference (Set 2 - Set 1):", set2 - set1)
  print("Symmetric Difference:", set1 ^ set2)

set_operations()
