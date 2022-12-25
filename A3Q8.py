A = [1,2,3,4,5]
set1 = set(A)
B = [2,4,6,8]
set2 = set(B)
C = [1,5,9,13,17]
set3 = set(C)
D = [1,2,3,4,5,6,7,8,9,10]
set4 = set(D)
print("Q8")
print("a :", end =" ")
print(set1 & set2)
print("b :" , end=" ")
print(set1 ^ set2 ^ set3)
print("c :" , end=" ")
print((set1 & set2)|(set3 & set2)|(set1 & set3))
print("d :" , end=" ")
print(set4 - set1)
print("e :" , end=" ")
print(set4-set1-set2-set3)