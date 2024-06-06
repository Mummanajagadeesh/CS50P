def main():
    greeting=input("Greeting:")
    print(f"${value(greeting)}")

def value(greeting):
    greet=greeting
    greet=greet.strip().lower()
    if "hello" not in greet:
        if greet[0]=='h':
            return 20
        else:
            return 100
    else:
        return 0

if __name__=="__main__":
    main()
