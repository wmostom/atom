# n = 99 squared # found the biggest possible square under 100
n = 99**99
# creating variable for n
digits = ([int(x) for x in str(n)])
# printing the sum of the digits for variable n
print sum(digits)
