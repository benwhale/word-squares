from pathlib import Path

import dawg

"""
This is a data preprocessing class for the word squares task.
It allows the user to index a dictionary into a Directed Acyclic Word Graph (DAWG), a highly space efficient data
structure which allows fast prefix search. This should allow the dictionary used to be scaled up to include many
more words if desired.
"""


class DictionaryDAWGIndexer:
    """
    I would have liked to refactor this into a more modular data access layer which could allow the data structure
    to be switched out - providing an abstract base class which could be inherited from, and access methods so that the
    classes using the DAWG could retrieve prefixes
    """

    @staticmethod
    def index_from_file(text_file):
        """
        Indexes data into a set of DAWGs for each word length between 1 and the longest word in the dictionary.
        :param text_file: the relative filename to open
        """

        with open(text_file) as dictionary:
            lines = dictionary.read().splitlines()  # Split lines without /n

            word_length_dict = {}
            max_length = len(
                max(lines, key=len)
            )  # Get the longest wrd in the dictionary

            for i in range(0, max_length):  # once for each word size for 1 to max
                # add a new key for this word length to the dictionary with an empty list
                word_length_dict[i + 1] = []

            for line in lines:
                # Append each word to the relevant dictionary
                word_length_dict[len(line)].append(line)

            for key, value in word_length_dict.items():  # length, [words]
                length_dawg = dawg.CompletionDAWG(value)

                save_location = Path(__file__).parents[
                    1
                ] / "indexed_data/{0}.dawg".format(key)

                length_dawg.save(str(save_location))
