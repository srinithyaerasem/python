n=int(input("Enter a number: "))
count=0

# if(n<2):
#     print("Not prime")
# else:
    
#     for i in range(2,n//2+1):
    
#         if n%i==0:
#             count+=1
#     if count==0:
#         print("prime")
#     else:
#         print("Not prime")
        
        #OR
        
if(n<2):
    print("Not prime")
else:
    for i in range(2,n):
        if n%i==0:
            
            count+=1
    if count==0:
        
            print("Prime")
    else:
        print("Not prime")
