

sentence = raw_input("Input a sentence:")

words = sentence.split()

for word in words:
    if word[0] in 'aeiou':
        print word + 'way'
    else:
        print word[1:] + word[0] + 'ay'

