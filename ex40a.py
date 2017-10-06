mystuff = {'apples': "I AM APPLES!"}
print mystuff['apples']

def apple():
    print "I AM APPLES!"

import mystuff
mystuff.apple()

def apple():
    print "I AM APPLES!"

tangerine = "Living relection of a dream"

import mystuff

mystuff.apple()
print mystuff.tangerine

mystuff['apple'] #get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangeringe # same thing, it's just a variable

class Mystuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

#dict style
mystuff['apples']

# module style
mystuff.apples()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine
