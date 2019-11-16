# Random Poem Generator 

## Concept 
The idea for this project is to make a simple poem generator.  Here's how I envision this program working:
1. The user will input the number of stanzas they want in their poem and the number of lines in each stanza.
2. The poem generator will randomly select a template line from the templates.txt file. Each template line is missing nouns, adjectives, adverbs, and verbs; the missing words are marked by a '1' for adjectives, a '2' for adverbs, a '3' for nouns, and a '4' for verbs. 
3. For each missing word, the poem generator will randomly select a noun, adjective, adverb, or verb from their respective lists and insert the missing word into the template line to get the complete line.
4. The generator will do this for each line, until it reaches the proper number of stanzas/lines. 
5. It will output the final result to the user. 

## Potential Challenges 

Because this is a very "brute-force" way to emulate a complex literary structure, the generated poem is not expected to make grammatical or semantic sense. Some probable difficulties in making the output poem a coherent piece:
- Verb tenses: the poem will randomly select verbs from a list of around 30,000 verbs. These verbs are of the present, past, and future tense; thus, the verb tense of the poem as a whole will most likely not be consistent
- Nouns: again, because the generator will be selecting nouns at random from a list of around 82,000 nouns, the context in which the nouns will be used may be non-sensical 
- Punctuation: some punctuation might be incorporated into the template files, but I'd have to figure out how to incorporate punctuation to the end of some lines (or at least to the last line of the poem). If I choose to randomize the punctuation (by placing random commas, dashes, or periods at the end of lines), then the cohesiveness and meaning of the poem could get more disjointed 

## Result 

As of November 16, 2019, the program accepts user input for the number of lines and stanzas and returns a poem that generates lines based off randomly selected templates for each line, and randomly selected words within each line. The user can choose whether or not they want to generate another poem after the first poem has been generated.

As expected, the generated poem makes very little sense semantically, has no punctuation, and has many grammar issues regarding tenses and possessives. I'm sure that there's also a more efficient way to get the poem to generate, since currently it utilizes what is essentially a 2D array (the generator iterates through a list of lines, and each line contains a list of words). However, it is still pretty interesting to see the unique ways in which the generator combines words and lines, even if semantically it might have no discernible meaning. 

## Ideas for Future Additions and Improvements 

As it stands, the project and program itself is very simple. However, there are many ways in which the project can be developed further and made more interesting and complex. Here are some of my ideas:

#### 1. Improving the grammar
Much of what ruins the readability of the generated poem has to do with the grammar. These are some of the common grammar errors that emerge from the current implementation of the poem generator:
- a vs an: for example, you might see "a apple", or "an book". One way to fix this is to add an article symbol in the template lines. If the program encounters this symbol, it'll peek ahead at the next word, and if the word starts with a vowel, it'll replace the symbol with "a", and if the word starts with a consonant, it'll replace the symbol with "an".
An example template line might look something like this:
      ```
      1) I 4 @ 3 with @ 1 3 
      ```
   The "@" symbol will get replaced with "a" or "an" depending on the succeeding word. 
- tenses -- past, future, present: there are many cases where verb tenses don't match. For example: "The bird flying and danced", "will pressures", "no judge could ever fortifying", etc. 
- singular vs plural: there are cases where these don't match up either. For example: "the earthquakes was", "there is no pumpkins", "a powerful energies", etc.    
- verbs preceeded by "to": many of the verbs are already conjugated, so you'd often see things like "to predicating", "to decreases", etc. 
- capitalization: some of the lines start with the noun/verb/adjective/adverb words, all of which are lowercase. However, the first letter of the word should be capitalized if it's the first word of the line.

One way in which some of these errors can be fixed is by editing the datasets of verbs and only keeping the verbs that are in the infinitive form (by removing the words with "-ing", "-ed", "-s" endings and manually removing any word that has an irregular past/present conjugation (such as the word "went" for the infinitive "to go"). Then, the generator could add the proper suffix to the infinitive form of the verb based on the word that preceeds it (for example, if our verb is "think", and the preceeding word is "to", the generator would do nothing and would append "to think" to the current line. But if the preceeding verb is a singular noun (ex. "brain"), it would append an "s" to the end of the verb and append "brain thinks" to the current line).  

There is also punctuation to consider. Currently, the poem has no punctuation since there are many considerations to take into account when it comes to punctuation. The punctuation could be built into the templates, which would probably be the simplest way to solve the issue. However, the punctuation at the very end of the line would have to be approached carefully -- we don't want to place a period at a random point and cause sentence fragments, and we don't want to place a comma at the end of the final line of the poem. 

#### 2. Allowing the user to save the poem to a file
A simple modification would be to allow the user to save the generated poem to a .txt file if they like the result. This will probably be the first thing I'll consider implementing, since it should be a fairly straightforward process. 
#### 3. Adding rhyme
Allowing the user to choose if they would like the generated poem to rhyme would make the poem more interesting. One way in which this could be done is to have the generator ensure that the last word of the line contains at least 4 or 5 matching ending characters with the last 4 or 5 characters of the last word in the preceeding line. The generator would have to keep track of the last word of the lines of the poem, which could be a bit challenging. Various rhyme schemes would make this more challenging as well -- for example, in an "aabb" rhyme scheme, the generator would only have to look at the previous line. However, in an "abab" rhyme scheme, the generator would have to look at the the line before the previous line.    
#### 4. Adding various types of poems
Right now, the poem that's generated can be considered free verse. However, the generator can be modified to output a poem in the style of a haiku, limerick, sonnet, etc. This is where our 1, 2, 3, and 4 syllable words lists could be handy. The user would choose which style of poem they'd like generated, and the program will generate that type of poem based on the specifications. 
#### 5. Adding a poem title 
Poems traditionally have titles, so another way to spice this project up would be to give the randomly generated poems a title. The easiest way in which this could be done is to simply prompt the user to give a title to the poem. We could make the program randomly generate a title as well, which would be a bit more difficult.    
#### 6. Adding a simple UI 
I have very little knowledge about this particular area, but it could be cool to set up a simple UI that would allow the user to interact with the program through buttons and dropdown menus for the poem options. This could probably be done with HTML and Javascript. 

## Acknowledgements
The words lists were obtained through the zip file provided on this site: 
http://www.ashley-bovan.co.uk/words/partsofspeech.html 
