import random

def get_input(minv,maxv):
    return int(raw_input("Enter an integer from %i to %i: " % (minv,maxv)))

min_value = 1
max_value = 99

secret_value = random.randint(min_value, max_value)

guess = get_input(min_value, max_value)
while secret_value != guess:
    if guess < secret_value:
        print "guess is low"
        guess = get_input(min_value, max_value)
    elif guess > secret_value:
        print "guess is high"
        guess = get_input(min_value, max_value)
print "you guessed it!"
