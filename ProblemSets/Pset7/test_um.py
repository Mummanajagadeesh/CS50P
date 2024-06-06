from um import count

def main():
    test_um()

def test_um():
    assert count("yummy")==0
    assert count("um...")==1

if __name__=="__main__":
    main()
