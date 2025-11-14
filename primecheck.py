n=(int(input("Enter a number")))
isprime=True
if(1>=n):
    isprime=False
else:
    for i in range(2,n):
        if(n%i==0):
            isprime=False
if(isprime):
    print("Given number is prime")
else:
    print("not prime")
    
