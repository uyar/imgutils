from pathlib import Path

from imgutils.size import get_aspect_ratio, get_height, get_width

CURRENT_DIR = Path(__file__).parent


def test_get_width_should_return_correct_width():
    assert get_width(CURRENT_DIR / "disco-dingo.png") == 1200


def test_get_height_should_return_correct_height():
    assert get_height(CURRENT_DIR / "disco-dingo.png") == 675


def test_get_aspect_ratio_should_return_correct_ratio():
    ratio = get_aspect_ratio(CURRENT_DIR / "disco-dingo.png")
    assert abs(ratio - (1200 / 675)) < 1e-12
