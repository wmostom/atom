i = 1
numbers = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Animals now: ", numbers
    print "At the bottom i is %d" % i


print "The Animals: "

for num in numbers:
    print num
