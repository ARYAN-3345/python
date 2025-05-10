a=int(input("Enter Number one :"))
b=int(input("Enter Number two :"))
c=int(input("Enter Number three :"))
d=int(input("Enter Number four :"))

if(a>b and a>c and a>d):
    print("greater number is :",a)
elif(b>a and b>c and b>d):
    print("greater number is :",b)
elif(c>a and c>b and c>d):
    print("greater number is :",c)    
else:
    print("greater number is :",d)