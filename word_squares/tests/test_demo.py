import pytest

from word_squares.solver.solver_service import SolverService


@pytest.fixture
def solver_service():
    return SolverService()


def test_example_1(solver_service):
    """
    rose
    oven
    send
    ends
    """
    result = solver_service.generate_word_square(4, "eeeeddoonnnsssrv")

    assert "".join(result[0]) == "rose"
    assert "".join(result[:, 0]) == "rose"
    assert "".join(result[1]) == "oven"
    assert "".join(result[:, 1]) == "oven"
    assert "".join(result[2]) == "send"
    assert "".join(result[:, 2]) == "send"
    assert "".join(result[3]) == "ends"
    assert "".join(result[:, 3]) == "ends"


def test_example_2(solver_service):
    """
    moan
    once
    acme
    need
    """
    result = solver_service.generate_word_square(4, "aaccdeeeemmnnnoo")

    assert "".join(result[0]) == "moan"
    assert "".join(result[:, 0]) == "moan"
    assert "".join(result[1]) == "once"
    assert "".join(result[:, 1]) == "once"
    assert "".join(result[2]) == "acme"
    assert "".join(result[:, 2]) == "acme"
    assert "".join(result[3]) == "need"
    assert "".join(result[:, 3]) == "need"


def test_example_3(solver_service):
    """
    feast
    earth
    armor
    stone
    threw
    """
    result = solver_service.generate_word_square(5, "aaaeeeefhhmoonssrrrrttttw")

    # The example given has more than one solution

    if "".join(result[2]) == "armer":
        assert "".join(result[0]) == "feast"
        assert "".join(result[:, 0]) == "feast"
        assert "".join(result[1]) == "earth"
        assert "".join(result[:, 1]) == "earth"
        assert "".join(result[2]) == "armer"
        assert "".join(result[:, 2]) == "armer"
        assert "".join(result[3]) == "steno"
        assert "".join(result[:, 3]) == "steno"
        assert "".join(result[4]) == "throw"
        assert "".join(result[:, 4]) == "throw"
    else:
        assert "".join(result[0]) == "feast"
        assert "".join(result[:, 0]) == "feast"
        assert "".join(result[1]) == "earth"
        assert "".join(result[:, 1]) == "earth"
        assert "".join(result[2]) == "armor"
        assert "".join(result[:, 2]) == "armor"
        assert "".join(result[3]) == "stone"
        assert "".join(result[:, 3]) == "stone"
        assert "".join(result[4]) == "threw"
        assert "".join(result[:, 4]) == "threw"


def test_example_4(solver_service):
    """
    heart
    ember
    above
    revue
    trees
    """
    result = solver_service.generate_word_square(5, "aabbeeeeeeeehmosrrrruttvv")

    assert "".join(result[0]) == "heart"
    assert "".join(result[:, 0]) == "heart"
    assert "".join(result[1]) == "ember"
    assert "".join(result[:, 1]) == "ember"
    assert "".join(result[2]) == "above"
    assert "".join(result[:, 2]) == "above"
    assert "".join(result[3]) == "revue"
    assert "".join(result[:, 3]) == "revue"
    assert "".join(result[4]) == "trees"
    assert "".join(result[:, 4]) == "trees"


def test_example_5(solver_service):
    """
    Warning, takes in the region of 90s to run this example on my Macbook - this test file takes about 01:53 in total
    bravado
    renamed
    analogy
    valuers
    amoebas
    degrade
    odyssey
    """
    result = solver_service.generate_word_square(
        7, "aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy"
    )

    assert "".join(result[0]) == "bravado"
    assert "".join(result[:, 0]) == "bravado"
    assert "".join(result[1]) == "renamed"
    assert "".join(result[:, 1]) == "renamed"
    assert "".join(result[2]) == "analogy"
    assert "".join(result[:, 2]) == "analogy"
    assert "".join(result[3]) == "valuers"
    assert "".join(result[:, 3]) == "valuers"
    assert "".join(result[4]) == "amoebas"
    assert "".join(result[:, 4]) == "amoebas"
    assert "".join(result[5]) == "degrade"
    assert "".join(result[:, 5]) == "degrade"
    assert "".join(result[6]) == "odyssey"
    assert "".join(result[:, 6]) == "odyssey"
