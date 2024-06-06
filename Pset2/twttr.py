def main():
    text=str(input("Input:"))
    print(shorten(text))

def shorten(word):
    word=str(word)
    test=""
    vowels=["a","e","i","o","u"]
    upper_vowels=[i.upper() for i in vowels]
    for i in range(len(word)):
        if (word[i] not in vowels) and (word[i] not in upper_vowels):
            test+=word[i]
    return test

if __name__=="__main__":
    main()
