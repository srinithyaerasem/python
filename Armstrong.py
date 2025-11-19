n = int(input("Enter a number: "))
sum = 0
temp = n
power= len(str(n))
while temp > 0:
    dig = temp % 10
    sum += dig ** power
    temp //= 10
if sum == n:
    print("Armstrong number")
else:
    print("Not Armstrong")
