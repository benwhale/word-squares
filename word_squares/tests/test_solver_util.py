from unittest.mock import Mock
from word_squares.solver.solver_util import SolverUtil


def test_get_words_matching_prefix():
    """
    Given a data structure implementing .keys()
    Expect that .keys() is called on the object, and that the value returned from that call is returned
    """
    mock_dawg = Mock()
    mock_dawg.keys.return_value = ["fond", "food"]
    result = SolverUtil.get_words_matching_prefix(mock_dawg, "fo")

    assert mock_dawg.keys.called
    assert result == ["fond", "food"]
