lst = list(map(int, input("Enter elements: ").split()))
if lst == lst[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
