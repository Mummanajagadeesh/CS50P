def main():

    time=input("What time is it?")
    if 7<=convert(time)<=8:
        print("breakfast time")
    elif 12<=convert(time)<=13:
        print("lunch time")
    elif 18<=convert(time)<=19:
        print("dinner time")


def convert(time):
    if ("a.m." not in time) and ("p.m." not in time) :
        hr,min=time.split(":")
        return float(hr)+(float(min)/60)
    elif "a.m." in time:
        hr,min_=time.split(":")
        min,bin=min_.split(" ")
        return float(hr)+(float(min)/60)
    elif "p.m." in time:
        hr,min_=time.split(":")
        min,bin=min_.split(" ")
        return float(hr)+12+(float(min)/60)
if __name__ == "__main__":
    main()
