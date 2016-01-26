#!/bin/usr/env python


VOWEL = ['a', 'e', 'i', 'o', 'u']


def pig_latin(word):
    if word[0] in VOWEL:
        word += 'way'
    else:
        word = word[1:] + 'ay'
    return word


test_str = ['air', 'eat', 'under', 'computer', 'floor', 'desk']

print test_str
for word in test_str:
    print pig_latin(word)


test_word  = raw_input("Input:")
print pig_latin(test_word)


print "Hello, {0:_^15}".format("Peter")

for x in VOWEL:
    if x == 'u':
        continue
else:
    print "END with nothing"