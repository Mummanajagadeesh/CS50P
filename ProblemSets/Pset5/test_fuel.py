from fuel import convert
from fuel import gauge
import pytest

def main():
    test_fuel()

def test_fuel():

    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")
    with pytest.raises(ValueError):
        assert convert("cat/cat")
    assert convert("2/3")==67 and gauge(67)=="67%"
    assert convert("0/100")==0 and gauge(0)=="E"
    assert convert("1/100")==1 and gauge(1)=="E"
    assert convert("100/100")==100 and gauge(100)=="F"
    assert convert("99/100")==99 and gauge(99)=="F"


if __name__=="__main__":
    main()
