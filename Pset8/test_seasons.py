from seasons import check_date

def main():
    test_date(0)

def test_date():
    assert check_date("1998-07-03")==("1998","07","03")
    assert check_date("2005-10-02")==("2005","10","02")
    assert check_date("2006-04-03")==("2006","04","03")

if __name__=="__main__":
    main()
