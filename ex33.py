i = 0
numbers = []

while i < 100:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 10
    print "Numners now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
