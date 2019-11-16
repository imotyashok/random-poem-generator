#########################################################################
##                      RANDOM POEM GENERATOR                      
## THE IDEA 
## - a program that generates poems by choosing random verbs, nouns, 
## adjectives, and adverbs, and inserting them into a built-in 
## template 
## 
## COMPONENTS 
## [✔] Lists of verbs, nouns, adjectives, and adverbs
## [✔] Some type of poem structure that contains the number of lines,
##     number of stanzas, and contents (?) of the poem
## [✔] Allow user to input number of lines and stanzas
## [✔] Function that generates the poem
## [✔] List of sentence structure templates, fill in the blank style
##     (I'll make the file for this myself) 
##########################################################################
from words import Words
import random
import time

def poem_generator(lines, stanzas, words):
    line_count = 0
    stanza_count = 0
    poem = []

    # This section retrieves the words lists. The way that templates
    # list works is that the nouns, verbs, adjectives, and adverbs stand
    # for numbers 3, 4, 1, and 2, respectively (as shown by the label below).
    # The function will replace the number that it encounters in the template
    # line with a random word that corresponds to it.
    nounList = words.get_nouns()        # 3
    verbList = words.get_verbs()        # 4
    adjList = words.get_adjectives()    # 1
    advList = words.get_adverbs()       # 2
    tempList = words.get_templates()

    while stanza_count < stanzas:
        tempLine = random.choice(tempList)
        poemLine = []
        if stanza_count < stanzas:
            for word in tempLine:
                if word == '1':
                    poemLine.append(random.choice(adjList))
                elif word == '2':
                    poemLine.append(random.choice(advList))
                elif word == '3':
                    poemLine.append(random.choice(nounList))
                elif word == '4':
                    poemLine.append(random.choice(verbList))
                else:
                    poemLine.append(word)

            poem.append(poemLine)
            line_count += 1
            if line_count % lines == 0:
                poem.append(' ')
                line_count = 0
                stanza_count += 1

    for line in poem:
        print(*line, sep = ' ')

def main():
    yes = True
    while yes:
        lines = int(input(">>> Enter the number of lines you'd like in a stanza: "))
        stanzas = int(input(">>> Enter the number of stanzas you'd like in your poem: "))
        words = Words()

        print("Generating poem...\n")
        time.sleep(1)

        poem_generator(lines, stanzas, words)

        repeat = input("\n>>> Would you like another poem? (yes/no) ").lower()
        if repeat == "y" or repeat == "yes":
            continue
        elif repeat == "n" or repeat == "no":
            yes = False
        else:
            print("Sorry, '%s' is not recognized. \n"%(repeat))
            yes = False

main()
