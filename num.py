# Python program to print positive Numbers in a given range
lwr_limit = int(input("Enter the start of range: "))
upr_limit = int(input("Enter the end of range: "))
# iterating each number in list
for num in range(lwr_limit, upr_limit + 1):
    # checking condition
    if num >= 0:
        print(num, end=" ")