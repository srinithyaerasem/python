lst = list(map(int, input("Enter numbers: ").split()))

big_even = None
big_odd = None

for num in lst:
    if num % 2 == 0:   # even number
        if big_even is None or num > big_even:
            big_even = num
    else:              # odd number
        if big_odd is None or num > big_odd:
            big_odd = num

print("Biggest Even:", big_even)
print("Biggest Odd:", big_odd)
