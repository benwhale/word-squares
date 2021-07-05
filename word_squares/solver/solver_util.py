class SolverUtil:
    """Quick util class to separate out the keys access from the actual result. With more time I would have refactored
    this with the dictionary_dawg_indexer to create a data access layer"""

    @staticmethod
    def get_words_matching_prefix(dawg, prefix):
        """
        Returns the words which start with the provided prefix
        :param dawg: The data object to retrieve from
        :param prefix: The prefix to search for
        :return: List of matching words
        """
        return dawg.keys(prefix)
