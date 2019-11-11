# Random Poem Generator 

## Concept 
The idea for this project is to make a simple poem generator.  Here's how I envision this program working:
1. The user will input the number of stanzas they want in their poem and the number of lines in each stanza.
2. The poem generator will randomly select a template line from the templates.txt file. Each template line is missing nouns, adjectives, adverbs, and verbs.
3. For each missing word, the poem generator will randomly select a noun, adjective, adverb, or verb from their respective lists and insert the missing word into the template line to get the complete line.
4. The generator will do this for each line, until it reaches the proper number of stanzas/lines. 
5. It will output the final result to the user. 

## Potential Challenges 

Because this is a very "brute-force" way to emulate a complex literary structure, the generated poem is not expected to make grammatical or semantic sense. Some probable difficulties in making the output poem a coherent piece:
- Verb tenses: the poem will randomly select verbs from a list of around 30,000 verbs. These verbs are of the present, past, and future tense; thus, the verb tense of the poem as a whole will most likely not be consistent
- Nouns: again, because the generator will be selecting nouns at random from a list of around 82,000 nouns, the context in which the nouns will be used may be non-sensical 
- Punctuation: some punctuation might be incorporated into the template files, but I'd have to figure out how to incorporate punctuation to the end of some lines (or at least to the last line of the poem). If I choose to randomize the punctuation (by placing random commas, dashes, or periods at the end of lines), then the cohesiveness and meaning of the poem could get more disjointed 
