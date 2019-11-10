#include <stdio.h>
#include <stdlib.h>
#include "poem.h"

poem_type new_poem(int stanzas, int lines, char** data)
{
    poem_type* poem = (poem_type*)malloc(sizeof(poem_type));
    poem->stanzas = stanzas;
    poem->lines = lines;
    // Figure out how to initialize array of strings... 
    
}