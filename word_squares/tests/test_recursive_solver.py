from unittest import mock
from unittest.mock import Mock

from word_squares.solver.recursive_solver import RecursiveSolver


@mock.patch("word_squares.solver.recursive_solver.RecursiveSolver.solve")
def test_generate_solution(mock_solve):
    """
    Given test_generate_solution is called
    Expect that solve is called with the expected initial values
    """

    mock_grid = Mock()
    mock_grid.copy.return_value = ["fake grid"]

    solver = RecursiveSolver(4, "abcdabcdabcdabcd", Mock(), mock_grid)
    solver.generate_solution()

    mock_solve.assert_called_with(
        word_no=0, letter_no=0, remaining_letters="abcdabcdabcdabcd", grid=["fake grid"]
    )


def test_solve_prefixes():
    """
    Given solve is called
    Expect that the methods to retrieve the horizontal and vertical prefixes are called with the correct letter/word
    number. Ditto for the search letters generation.
    """
    pass


def test_solve_control_flow():
    """
    Tests validating that the logic in the letter loop behaves as expected for various paths.
    Would be easier to test if the loop logic were to be refactored into its own method.
    """
    pass


def test_proceed_with_solution():
    """
    Test paths call solve or return the grid for:
    1. Letter number less than the dimension - 1
    2. Word number less than the dimension - 1
    3. Final solution found
    """
    pass


def test_find_valid_words():
    """
    Test expected util methods are called and the return value is as expected.
    """
    pass


def test_place_letter():
    """
    Test the two Value error raising cases, and test that the diagonal returns a new letter string with one fewer letter,
    and the other cases return a letter string with two fewer.
    Test that the grid is in the state expected
    """
    pass


def filter_words_to_contain_letters():
    """
    Test that a given array of words results in a yielded array only containing words
    which can be made up of letters in the class letters property
    """
    pass


def test_get_horizontal_prefix():
    """
    Test that an empty, partially filled and fully filled numpy array row returns the correct string
    """
    pass


def test_get_vertical_prefix():
    """
    Test that an empty, partially filled and fully filled numpy array column returns the correct string
    """
    pass


def test_get_unique_letters():
    """
    Given a string
    Expect that an alphabetically sorted list with a single instance of each letter is returned
    """
