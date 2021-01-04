"""Randomly selects a pseudonym."""
import sys
import random

print ("Welcome to the Psych 'Sidekick Name Picker.'\n")
print ("A name just like Sean would pick for Gus:\n\n")

first = ('Wendy','Roland','Agnes','Daisy','Skids','Zoey','Rex','Jim','Ashcan','Jenny')

last = ('Adams','Banks','Baker','Walker','OToole','Samaras','Murphy','Culver','Pete','Barnes')

middle = ("\"The Biggun\"","\"Tiny\"", "\"The Mac\"", "\"Special Sauce\"", "\"Orange Tits\"")

"""Functional Loop"""
while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    middleName = random.choice(middle)

    print("\n\n")
    if random.random() > 0.2:
        print("{} {}".format(firstName,lastName), file=sys.stderr)
    else:
        print("{} {} {}".format(firstName,middleName,lastName), file=sys.stderr)
    print("\n\n")

    try_again= input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break

input("\n Press Enter to exit.")
