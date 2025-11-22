a=[2,4,3,6,8,1,9,3,8]
max1=0
max2=0
for i in range(0,len(a)):
    if(a[i]>max1):
        max2=max1
        max1=a[i]
print("The second largest element in the list is:",max2)
