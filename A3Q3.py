a=int(input("1st no."))
b=int(input("2nd no."))
print("number is between a and b")
print([(x,x**2) for x in range(a,b+1)])