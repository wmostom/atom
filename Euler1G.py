def answer3(a): #returns if a is divisible by 3
    return a % 3 == 0

def answer5(a): #returns if a is dividible by 5
    return a % 5 == 0

def finalanswer(a): # adds together all of the returned values of answer3 and answer5.
    z = 0 #setting a starting point a 0
    for i in range(0,a): # creating term i by setting its range from 0 to whatever "a" comes out to be.
        if answer3(i) or answer5(i): # this says that answer3 and answer5 must be fitting in the range that we set for i
            z += i # this is adding all of the mulitiples of 3 and 5 in a
    return z # This is giving the value of z

print finalanswer(1000) # this states that we must print the answers with in 1000
