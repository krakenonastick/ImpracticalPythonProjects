"""Map letters from a string into dictionary & print bar chart of frequency"""
import sys
import pprint
from collections import defaultdict

#Note: txt should be a short phrase for bars to fit in window
TEXT = 'Like the castle in its corner in a midieval game, I foresee terrible \
trouble and I stay here just the same.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

mapped = defaultdict(list,{ k:[] for k in ('a','b','c','d','e','f','g',
                                           'h','i','j','k',
                                           'l','m','n','o','p','q','r','s','t',
                                           'u','v','w','x','y','z') })
mapped.fromkeys(['q', 2, 3, 4])
for character in TEXT:
    if character in ALPHABET:
        mapped[character].append(character)

print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text= ", end='')
print("{}\n".format(TEXT), file=sys.stderr)
pprint.pprint(mapped, width=110)
