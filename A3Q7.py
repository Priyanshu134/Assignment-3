n=int(input("enter no. upto which you want to ge the series"))
n1=0
n2=1
sum=0
if n<=0:
    print("enter no. greater than 0")
else:
    for i in range(0,n):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2
