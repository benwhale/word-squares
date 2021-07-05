import dawg
import numpy as np
from pathlib import Path

from word_squares.solver.recursive_solver import RecursiveSolver


class SolverService:
    """
    Service class to handle input validation and data loading, as well as calling the solver to build a solution.
    """

    word_dawg = dawg.CompletionDAWG()

    def generate_word_square(self, dimension: int, letters: str):
        """
        Controls the square generation process. Validates input, loads the relevant
        indexed data structure and initialises an empty grid.
        :param dimension: integer representing the length of the sides of the word square.
        :param letters: string containing the letters to fit into the square.
        :return: a populated numpy array where a solution is found, or False where one can not be found.
        """

        self.validate(dimension, letters)
        self.load_dawg(dimension)
        grid = np.full((dimension, dimension), "", dtype=str)

        solver = RecursiveSolver(dimension, letters, self.word_dawg, grid)
        solution = solver.generate_solution()

        return solution

    def validate(self, dimension, letters):
        """
        Validation method to check that the length of the provided letter string matches the expected
        number of values from the provided dimension. Raises ValueError when the value is not valid.
        """
        expected_letter_count = pow(dimension, 2)
        letter_count = len(letters)

        if not expected_letter_count == letter_count:
            raise ValueError(
                "Number of provided letters does not match the provided square dimensions"
            )

    def load_dawg(self, dimension):
        """
        Attempts to load a DAWG from the indexed data directory. If one is not found then it will raise an exception.
        """
        # Use pathlib to make path work on windows as well as unix based os
        filename = Path(__file__).parents[1] / "indexed_data/{0}.dawg".format(dimension)

        if not filename.exists():
            raise FileNotFoundError(
                "Unable to find corresponding indexed data file for this problem. Have you run the index_data command?"
            )

        self.word_dawg.load(str(filename))
