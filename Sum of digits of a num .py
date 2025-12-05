# input = 12345
# output = 1+2+3+4+5 = 15

number = 12345
Digits = [int(d) for d in str(number)]
sum_nums = sum(Digits)
print(sum_nums)