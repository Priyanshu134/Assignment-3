a=int(input("Date"))
b=int(input("Month"))
c=int(input("Year"))
if 1800<=c<=2025 and 1<=b<=12 and 1<=a<=31:
    if b==2 and 1<=a<=27:
        print(a+1,"/",b,"/",c)
    elif b==2 and a==29 and c%4==0:
        print(1,"/",3,"/",c)
    elif b==2 and a==28:
        print(1,"/",3,"/",c)
    elif b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12 and 1<=a<=30:
        print(a+1,"/",b,"/",c)
    elif b==1 or b==3 or b==5 or b==7 or b==8 or b==10 and a==31:
        print(1,"/",b+1,"/",c)
    elif a==31 and b==12:
        print(1,"/",b,"/",c+1)
    elif b==4 or b==6 or b==9 or b==11 and 1<=a<=29:
        print(a+1,"/",b,"/",c)
    elif b==4 or b==6 or b==9 or b==11 and a==30:
        print(1,"/",b+1,"/",c)
    else:
        print("Date not valid")
else:
    print("date not valid")


