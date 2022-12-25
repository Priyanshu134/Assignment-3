fib = [1,1]
print("input upto which number sequence is required :" , end=" ")
n = int(input())
Sum = 2
length = 2
for i in range(3,n+1) :
    fib.append(fib[i-3]+fib[i-2])
    Sum += fib[i-1]
    length += 1
if n == 1 :
    print([1])
    print(1.0)
else :

    print(fib)
    print(Sum/length)