from working import convert
import sys
import pytest

def main():
    test_wrong()


def test_wrong():
    # assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    # assert convert("10 PM to 8 AM")=="22:00 to 8:00"
    with pytest.raises(ValueError):
        convert("13 AM - 17 PM")
    # with pytest.raises(ValueError):
    #     convert("9:60 AM - 9:60 PM")


if __name__=="__main__":
    main()
