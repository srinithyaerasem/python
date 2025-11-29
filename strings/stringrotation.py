def is_rotation(a,b):
    return len(a)==len(b) and b in a+a
a=input("Enter a string: ")
b=input("Enter a string: ")
print("1:", is_rotation(a,b))
