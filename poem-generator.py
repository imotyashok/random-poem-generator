NOUNS = "nouns/nouns.txt"
VERBS = "verbs/verbs.txt"
ADJECTIVES = "adjectives/adjectives.txt"
ADVERBS = "adverbs/adverbs.txt"
TEMPLATES = "templates.txt"

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

def get_nouns(NOUNS):
    # Makes a list of all the nouns
    with open(NOUNS, newline = '') as file:
        nouns = [line.strip() for line in file]

    return nouns

def get_verbs(VERBS):
    # Makes a list of all the verbs
    with open(VERBS, newline = '') as file:
        verbs = [line.strip() for line in file]

    return verbs

def get_adjectives(ADJECTIVES):
    # Makes a list of all the adjectives
    
    with open(ADJECTIVES, newline = '') as file:
        adjectives = [line.strip() for line in file]

    return adjectives

def get_adverbs(ADVERBS):
    # Makes a list of all the adverbs
    with open(ADVERBS, newline = '') as file:
        adverbs = [line.strip() for line in file]

    return adverbs

def get_templates(TEMPLATES):
    # Puts all the template contents into a 2D array (list of lists)
    with open(TEMPLATES, newline = '') as file:
        templates = [line.strip().split() for line in file]

    print(*templates,sep="\n")


##def poem_generator_test(lines, stanzas, content):
##    line_count = 0
##    stanza_count = 0
##    poem = []
##    
##    for line in content:
##        # This properly separates the poem into stanzas based on the number
##        # of lines in each stanza, and the number of stanzas; the actual poem generator
##        # will randomly select lines from the templates list 
## 
##        if stanza_count < stanzas:
##            poem.append(line)
##            line_count += 1 
##            if line_count % lines == 0:
##                poem.append(" ")
##                line_count = 0
##                stanza_count += 1
##
##    return poem

def poem_generator(lines, stanzas):
    pass
    
def main():
    LINES = 3
    STANZAS = 2
    

main()







