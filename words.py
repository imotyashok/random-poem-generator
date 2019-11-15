##############################################################################
# Class that allows creation of Words() object so that it would be easy
# to get the lists from the files; currently we can get lists of nouns,
# verbs, adverbs, adjectives, and templates. For a simple random poem
# generator, this is all we need; however, I may consider implementing
# the syllable lists of each noun/verb/adjective/adverb file, with which
# we can do some interesting things in the poem generator.
##############################################################################

class Words:
    def __init__(self):
        self.nouns_f = "nouns/nouns.txt"
        self.verbs_f = "verbs/verbs.txt"
        self.adjectives_f = "adjectives/adjectives.txt"
        self.adverbs_f = "adverbs/adverbs.txt"
        self.templates_f = "templates.txt"

    def get_nouns(self):
        with open(self.nouns_f, newline='') as file:
            nouns = [line.strip() for line in file]
        return nouns

    def get_verbs(self):
        with open(self.verbs_f, newline='') as file:
            verbs = [line.strip() for line in file]
        return verbs

    def get_adjectives(self):
        with open(self.adjectives_f, newline='') as file:
            adjectives = [line.strip() for line in file]
        return adjectives

    def get_adverbs(self):
        with open(self.adverbs_f, newline='') as file:
            adverbs = [line.strip() for line in file]
        return adverbs

    def get_templates(self):
        with open(self.templates_f, newline='') as file:
            templates = [line.strip().split() for line in file]
        return templates
# def main():
#     word = Words()
#     tList = word.get_templates()
#     print(*tList,sep = '\n')
# main()
# main()