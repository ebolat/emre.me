# Check if the integer is even or odd
def even_or_odd_checker(num: int) -> str:
    if (num & 1) == 0:
        return f"{num} (decimal) = {bin(num)} (binary) and it is an EVEN number"
    else:
        return f"{num} (decimal) = {bin(num)} (binary) and it is an ODD number"


# Check if n-th bit is set
def check_nth_bit(num, n: int) -> str:
    if num & (1 << n):
        return f"{num} (decimal) = {bin(num)} (binary) and {n}th bit is set"
    else:
        return f"{num} (decimal) = {bin(num)} (binary) and {n}th bit is NOT set"


# Set n-th bit (if it is not already set)
def set_nth_bit(num, n: int) -> str:
    if num & (1 << n):
        return f"{num} (decimal) = {bin(num)} (binary) and {n}th bit is ALREADY set"
    else:
        set_nth_bit_result = num | (1 << n)
        return f"{num} (decimal) = {bin(num)} (binary). {n}th bit is changed and the result is: {bin(set_nth_bit_result)}"


print(even_or_odd_checker(1547548))
print(check_nth_bit(175, 5))
print(set_nth_bit(233, 2))
