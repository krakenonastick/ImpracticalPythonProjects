"""take a word as input and return the pig latin version of it."""

while True:
    #take word
    VOWELS = 'aeiouy'

    input_word = input("Please enter a word to pig latinify.\n")

    if input_word[0] in VOWELS:
        answer_Word = input_word + 'way'
    else:
        first_letter= input_word[0]
        sliced_word = input_word[1:]
        answer_Word = "{}{}{}".format(sliced_word,first_letter,"ay")
    #print word
    print("{}".format(answer_Word))

    try_again= input("\n\nTry again? (Press Enter else n to quit)\n ")

    if try_again.lower() == "n":
        break

input("\n Press Enter to exit.")
