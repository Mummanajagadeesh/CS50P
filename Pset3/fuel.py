def main():
    fraction=str(input("Fraction:"))
    print(gauge(convert(fraction)))


def convert(fraction):
    while True:
        try:
            frac=fraction
            x=int(frac[:frac.find("/")])
            y=int(frac[frac.find("/")+1:])
            if x<=y:
                return (round((eval(str(x)+"/"+str(y)))*100))
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"

if __name__=="__main__":
    main()
