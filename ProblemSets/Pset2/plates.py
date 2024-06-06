def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    char_in_plate=[i for i in s if i.isalpha()==True]
    num_in_plate=[i for i in s if i.isdigit()==True]
    str1="".join(char_in_plate)
    str2="".join(num_in_plate)
    if len(char_in_plate)>1 and len(s)<=6 and s==(str1+str2):
        if len(str2)>0:
            return True if int(str2[0])>0 else False
        else:
            return True
    else:
        return False
if __name__=="__main__":
    main()
