s = input("Enter a string: ")
vow = 0
cons=0


vowels = "aeiouAEIOU"

for ch in s:
    if ch in vowels:
        vow += 1
    else:
        cons+=1
        

print("total vowels in the given string are:",vow)
print("total consonants  in the given string are:",cons)
