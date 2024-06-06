import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit(0)


def validate(ip):
    if re.search(r'^[0-9]+\.[0-9]+\.[0-9]+\.([0-9]+(\.)?)$',ip):
        for i in ip.split("."):
            try:
                if int(i)<0 or int(i)>255:
                    return False
            except ValueError:
                pass

        return True
    else:
        return False

if __name__ == "__main__":
    main()
