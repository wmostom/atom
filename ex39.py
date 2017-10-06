things = ['a', 'b', 'c', 'd']
print things[1]

things[1] = 'z'
print things[1]

things
['a', 'z', 'c', 'd']
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print stuff['name']

print stuff['age']

print stuff['height']

stuff['city'] = "San Francisco"
print stuff['city']

stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff[1]

print stuff[2]

stuff
{'city': 'San Francisco', 2: 'Neato', 'name': 'Zed', 1: 'Wow', 'age': 39, 'height': 74}
