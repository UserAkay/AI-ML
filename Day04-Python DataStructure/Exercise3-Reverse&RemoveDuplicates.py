listA = [1, 5, 2, 6, 6, 3]

listA.reverse()

listB = list(set(listA))

print("Original reversed list: ",listA)
print("After removing duplicates: ", listB)