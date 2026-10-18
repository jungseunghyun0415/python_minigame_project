from utils import format_title


def test_format_title():
    assert format_title("행맨") == "=== 행맨 ==="


def test_format_title_empty():
    assert format_title("") == "===  ==="
