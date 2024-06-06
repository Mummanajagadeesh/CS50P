import re
import sys


def main():
    print(parse(input("HTML: ")))
    #parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>')


def parse(s):

    try:
        matches=re.search(r"src=\"(.+)\"",s)
        match=matches[1]
        match=match.replace("youtube.com","youtu.be")
        match=match.replace("/embed","")
        match=match.replace("www.","")
        if "https" not in match:
            match=match.replace("http","https")
        if "youtu.be" in match:
            return match
        else:
            return "None"
    except:
        return "None"

if __name__ == "__main__":
    main()
