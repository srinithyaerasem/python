n1=0
n2=1
n=int(input("Enter a number"))
print(n1,"\n",n2)
for i in range(2,n):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
