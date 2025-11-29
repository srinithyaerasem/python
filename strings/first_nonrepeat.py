def first_non_repeat(s):
    for c in s:
        if s.count(c)==1:
            return c
a=input("Enter a string: ")
print(first_non_repeat(a))
