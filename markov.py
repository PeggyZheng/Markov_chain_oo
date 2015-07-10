import sys
from random import choice


class SimpleMarkovGenerator(object):


    def read_files(self, file_list): #do we need a second argument here for file name(s)?
        """Given a list of files, make chains from them.
        Currently only taking the first file specified in the terminal
        """
        text_string = ""
        #files_to_string = list(sys.argv[1:])
        for file_path in file_list:
            read_the_file = open(file_path)
            for line in read_the_file:
                text_string += line.rstrip("\n") + " "


        return text_string


    def make_chains(self, corpus): #just need to sort out opening the string, 
    #splitting string into list of words
        """Takes input text as string; stores chains.
        Need to take the text_string from read_files, and need to supply
        the file name when we call that method to start this method. 

        """
        #corpus = self.read_files()
        chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)
        return chains
        # your code here
        # ultimately returns a dictionary
        # stores chainsSimpleMarkovGenerator (as opposed to creating them)
        # calls read_files before getting into its primary function

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""
        #chains = self.make_chains()
        key = choice(chains.keys())
        #print key
        words = [key[0], key[1]]
        #print words
        while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        return " ".join(words)


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    file_list = sys.argv[1:]

    random_sentence = SimpleMarkovGenerator()
    concat_string = random_sentence.read_files(file_list) 
    markov_dict = random_sentence.make_chains(concat_string)
    print random_sentence.make_text(markov_dict)

