from math import factorial #entering math and taking the factorial function out

def answer(): #defining a term called answers, on the lines below i am setting it equal to n and r
    n = 40     # The total numbers of moves possible to the right and down
    r = 20  # The total number of right moves for a path
    print factorial(n) / factorial(r) * factorial(r) # taking the factorial of 40 and diviing
# it by the factorial of 20. Then multiplying it by factorial of 20

answer()
