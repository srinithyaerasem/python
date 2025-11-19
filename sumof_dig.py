n=int(input("Enter a number"))
sum=0
for i in range(n):
    if n>0:
        dig=n%10
        sum+=dig
        n//=10
print("sum of the given number is: ",sum)
