#########################################################################
##                      RANDOM POEM GENERATOR                      
## THE IDEA 
## - a program that generates poems by choosing random verbs, nouns, 
## adjectives, and adverbs, and inserting them into a built-in 
## template 
## 
## COMPONENTS 
## [✔] Lists of verbs, nouns, adjectives, and adverbs
## [ ] Some type of poem structure that contains the number of lines,
##     number of stanzas, and contents (?) of the poem 
## [ ] Function that initializes a poem structure 
## [ ] Function that populates the poem structure with content 
## [ ] Function that prints out the poem to the screen
## [✔] List of sentence structure templates, fill in the blank style
##     (I'll make the file for this myself) 
##########################################################################
from words import Words

# def poem_generator_test(lines, stanzas, content):
#    line_count = 0
#    stanza_count = 0
#    poem = []
#
#    for line in content:
#        # This properly separates the poem into stanzas based on the number
#        # of lines in each stanza, and the number of stanzas; the actual poem generator
#        # will randomly select lines from the templates list
#
#        if stanza_count < stanzas:
#            poem.append(line)
#            line_count += 1
#            if line_count % lines == 0:
#                poem.append(" ")
#                line_count = 0
#                stanza_count += 1
#
#    return poem

def poem_generator(lines, stanzas, words):
    line_count = 0
    stanza_count = 0
    poem = []

    nounList = words.get_nouns()
    verbList = words.get_verbs()
    adjList = words.get_adjectives()
    advList = words.get_adverbs()
    tempList = words.get_templates()



def main():
    # Lines and stanzas are hardcoded for now for testing purposes, but
    # will be able to be input by the user later
    lines = 3
    stanzas = 2
    words = Words()

    poem_generator(lines, stanzas, words)

main()
