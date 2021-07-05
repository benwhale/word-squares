from word_squares.solver.solver_util import SolverUtil
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler("word_squares.log", mode="w")
fh.setLevel(logging.INFO)
logger.addHandler(fh)


class RecursiveSolver:
    def __init__(self, dimension, letters, dawg, grid):
        self.dimension = dimension
        self.letters = letters
        self.dawg = dawg
        self.grid = grid

    def generate_solution(self):
        """
        Makes the initial call to solve to kick off the recursive solving process.
        :return: Populated numpy array or False
        """
        return self.solve(
            word_no=0,
            letter_no=0,
            remaining_letters=self.letters,
            grid=self.grid.copy(),
        )

    def solve(self, word_no, letter_no, remaining_letters, grid):
        """
        Recursive solving function to traverse the grid.
        Retrives the prefixes for which go through this space on the grid.
        Iterates through the available letter choices and retrieves valid words combining the prefixes with the letter
        If there are valid words on both the vertical and horizontal axes, attempt to place the letters and move to the
        next space in the solution if successful. Returns False if there are no valid letters which can be placed at all
        or returns the result of the recursive calls to solved.
        """
        logger.info(grid)
        logger.info("searching for ({0},{1})".format(word_no, letter_no))
        horizontal_prefix = self.get_horizontal_prefix(word_no, grid)
        vertical_prefix = self.get_vertical_prefix(letter_no, grid)

        logger.debug(remaining_letters)
        search_letters = sorted(
            list(set(remaining_letters))
        )  # We only want to try each available letter once per iteration.
        # Putting it back into a sorted list allows for more predictability

        for letter in search_letters:
            logger.info("letter: {0}".format(letter))

            horiz_words, vert_words = self.find_valid_words(
                letter, horizontal_prefix, vertical_prefix
            )

            if len(horiz_words) == 0 or len(vert_words) == 0:
                continue  # Exit iteration - no valid words in either the horizontal or vertical for this letter choice

            try:
                updated_grid, solution_remaining_letters = self.place_letter(
                    word_no, letter_no, letter, remaining_letters, grid.copy()
                )
                logger.debug(
                    "remaining letters: {0}".format(solution_remaining_letters)
                )
            except ValueError:
                continue  # Exit iteration - We have tried to place more of a letter than there is remaining

            solution = self.proceed_with_solution(
                letter_no, word_no, solution_remaining_letters, updated_grid
            )

            if solution is False:
                continue  # Exit iteration - No solution down this route, so back up a step
            else:
                return solution
        return False  # We have reached the end of the letter iteration and there are no valid letters

    def proceed_with_solution(
        self, letter_no, word_no, solution_remaining_letters, updated_grid
    ):
        """
        Checks which letter we are on and works out which letter to solve for next.
        If we are mid way through a word, we try and complete that word with the next letter
        If we have completed a word, we move to the next word where there is one, and start at
        the first unfinished letter.
        Otherwise, we have filled in every slot and can return our solution up the chain.
        """
        if letter_no < self.dimension - 1:
            # Attempt to complete a given word first
            return self.solve(
                word_no,
                letter_no + 1,
                solution_remaining_letters,
                updated_grid.copy(),
            )
        elif word_no < self.dimension - 1:
            # Move onto the next word
            return self.solve(
                word_no + 1,
                word_no + 1,
                solution_remaining_letters,
                updated_grid.copy(),
            )
        elif word_no == self.dimension - 1 and letter_no == self.dimension - 1:
            # We have completed the final letter
            return updated_grid  # Return the final numpy array

    def find_valid_words(self, letter, horizontal_prefix, vertical_prefix):
        """
        Gets words matching both the horizonal and vertical prefixes, and filters to only include words which can be
        made by the remaining letters.
        :param letter: the character to add to the prefix
        :param horizontal_prefix: the horizontal prefix representing the letters placed in a row so far
        :param vertical_prefix: the vertical prefix representing the letters placed in a column so far
        :return: a tuple containing two lists with the matching horizontal and vertical words in them.
        """
        horiz_words = SolverUtil.get_words_matching_prefix(
            self.dawg, (horizontal_prefix + letter)
        )
        vert_words = SolverUtil.get_words_matching_prefix(
            self.dawg, (vertical_prefix + letter)
        )

        horiz_words = list(
            self.filter_words_to_contain_letters(horiz_words)
        )  # pass in prefix and the remaining words?
        vert_words = list(self.filter_words_to_contain_letters(vert_words))
        logger.info("words found")
        logger.debug(horiz_words)
        logger.debug(vert_words)
        return horiz_words, vert_words

    def place_letter(self, word_no, letter_no, letter, remaining_letters, grid):
        """
        Attempts to place letters in the current slot, and in it's mirror on the diagonal axis.
        If it is the diagonal axis then we only place the one. Placed letters are removed from the list.
        If this fails due to there not being enough letters to remove, we raise the ValueError onwards so
        that the parent method can handle it
        :param word_no: The current word number we are solving
        :param letter_no: The current letter number we are solving
        :param letter: The letter we are trying to place
        :param remaining_letters: The remaining letters available to place
        :param grid: The grid to place letters into
        :return: Updated grid and remaining letters if successful, raised ValueError if not
        """
        if word_no == letter_no:
            # We are on the diagonal axis, so there will only be one letter placed
            grid[word_no, letter_no] = letter
            try:
                letter_list = list(remaining_letters)
                letter_list.remove(letter)
                new_remaining_letters = "".join(letter_list)
            except ValueError:
                raise
        else:
            grid[word_no, letter_no] = letter
            grid[letter_no, word_no] = letter
            try:
                letter_list = list(remaining_letters)
                letter_list.remove(letter)
                letter_list.remove(letter)
                new_remaining_letters = "".join(letter_list)
            except ValueError:
                raise
        return grid, new_remaining_letters

    def filter_words_to_contain_letters(self, word_list):
        """
        First cut of a generator function to reduce the number of options to eliminate words
        which don't exist in the letter set.
        Will miss lots of invalid ones, but it's a start.
        Could do with a refactor to use the prefixes / remaining letters
        """
        for word in word_list:
            sorted_letters = sorted(self.letters)
            # Copy of letters string in list form

            for letter in word:
                try:
                    sorted_letters.remove(letter)
                except ValueError:
                    break
            else:
                # Runs when the loop is complete without breaking out
                yield word

    def get_horizontal_prefix(self, row_no, grid):
        """
        Retrives the currently generated prefix by joining the values in the specified row
        :param row_no: the row number to retrieve the prefix from
        :param grid: the grid to retrieve from
        :return: string containing the generated prefix
        """
        row = grid[row_no]
        return "".join(row)

    def get_vertical_prefix(self, col_no, grid):
        """
        Retrives the currently generated prefix by joining the values in the specified row
        :param col_no: the column number to retrieve the prefix from
        :param grid: the grid to retrieve from
        :return: string containing the generated prefix
        """
        col = grid[:, col_no]
        return "".join(col)
