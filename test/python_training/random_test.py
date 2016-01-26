import random
import sys

r = random.randint(1, 100)
u = raw_input("Guess the random number:")
# u = sys.stdin.readline()
print type(u)
u = int(u)
if u < r:
    print "too low"
elif u > r:
    print "too high"
else:
    print "right"

