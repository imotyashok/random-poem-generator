NOUNS = "nouns.txt"
VERBS = "verbs.txt"
ADJECTIVES = "adjectives.txt"
ADVERBS = "adverbs.txt"
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
## [ ] List of sentence structure templates, fill in the blank style
##     (I'll make the file for this myself) 
##########################################################################

def get_nouns(NOUNS):
    pass

def get_verbs(VERBS):
    pass

def get_adjectives(ADJECTIVES):
    pass

def get_adverbs(ADVERBS):
    pass

def get_templates(TEMPLATES):
    pass

def test_poem():
    # this is meant to simulate the template list that the poem
    # function will be pulling from
    
    test_content = ["test line 1",
                    "test line 2",
                    "test line 3",
                    "test line 4",
                    "test line 5",
                    "test line 6"]

    return test_content

def poem_generator_test(lines, stanzas, content):
    line_count = 0
    stanza_count = 0
    poem = []
    
    for line in content:
        # This properly separates the poem into stanzas based on the number
        # of lines in each stanza, and the number of stanzas; the actual poem generator
        # will randomly select lines from the templates list 
 
        if stanza_count < stanzas:
            poem.append(line)
            line_count += 1 
            if line_count % lines == 0:
                poem.append(" ")
                line_count = 0
                stanza_count += 1

    return poem
    
def main():
    LINES = 3
    STANZAS = 2
    testContent = test_poem()

    testPoem = poem_generator_test(LINES, STANZAS, testContent)
    print(*testPoem, sep = '\n')

main()







