print((5+5+5+5+5+5+5) / 5)

print((5*5*5) - 3)

print "ADI is Awesome."

print "%s" % ("True")

a = 10
b = "Awesome"
c = [1, 2, 3, 4, 5]
d = ("hi", "there", "Python!")
e = {"star" : 7, "fish" : "chips", "house" : "cards"}
f = {0, 1, 2, 5}

print type(a) is int
print a < 15

# Prints "True" if b is a string
print type(b) is str
print b[5] == 'm' and b[0] == "A"

# Prints "True" if c is a list
print type(c) is list 
print len(c) == 5
print 5 in c

# Prints "True" if d is a tuple
print type(d) is tuple
print d[2] == "Python!"

# Prints "True" if e is a dictionary
print type(e) is dict
print "star" in e
print 7 in e.values()
print e.get("fish") == "chips"
print len(e) == 3
e["house"] = "cards"
print len(e) == 3

# Prints "True" if f is a set
print type(f) is set
print len(f) == 4
print len(f & {2,5,7}) == 2

a = [1, 2, 3, 0, 5]

# Will your "a" variable pass my evil tests?

# Let's start off simple.  Is it the right type?
# Muhahahahaha!
if type(a) is list:
    print True
else:
    print False

# Didn't see this coming, did you?
for x in a:
    if not type(x) is int:
        print False
    else:
        print True

# And now, my evil for loop of evil testingness!
for y in range(a[3]):
    if y in a:
        print False

# Don't fall for my "Python Infinite Pit"!!!
try:
    a[5] = "Trap!"
    while True:
        print False
except IndexError:
    print True


# Write the "square" function here
def square(a):
	return a * a

# Write the "squarify" function here
def squarify(*args):
	sqr = []
	l = len(args)
	tup = (*args)
	#while x != l:
	for i in range(len(args)):
		s = square(tup[i])
		sqr.append(s)
	return sqr

# Don't edit anything below this comment
# --------------------------------------

print square(4) == 16
print square(square(3)) == 81
print squarify([3,4,9]) == [9, 16, 81]