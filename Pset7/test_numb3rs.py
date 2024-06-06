def main():

    test_true()
    test_false()
    sys.exit(0)

def test_true():

    assert validate("127.0.0.1")==True
    assert validate("255.255.255.255")==True

def test_false():

    assert validate("256.255.255.255")==False
    assert validate("1.2.3.1000")==False
    assert validate("cat")==False

if __name__=="__main__":
    main()
