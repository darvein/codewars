# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    res = ""
    for n in str(num): res += str(int(n)**2)
    return int(res)

print(square_digits(9119))
print(square_digits(0))
