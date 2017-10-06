
Regions = {
    'West': 'W',
    'Midwest': 'MW',
    'Northeast': 'NE',
    'South': 'S',
}


states = {
    'W': 'Colorado',
    'MW': 'Minnesota',
    'NE': 'Maine',
    'S': 'Florida'
}


cities['W'] = 'Denver'
cities['MW'] = 'Minneapolis'

#print out some cities
print '-' * 10
print "W Region has: ", cities['W']
print "MW Region has: ", cities['MW']

# print some states
print '-' * 10
print "South abbreviation is: ", Region['South']
print "Northeast abbreviation is: ", states['Northeast']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s"  % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might noy be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

#get a city with default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
x
