import emoji
test=str(input("Input:"))
print("Output:",end="")
if "thumbsup" in test:
    test=test.replace("thumbsup","thumbs_up")
if "earth_asia" in test:
    test=test.replace("earth_asia","globe_showing_Asia-Australia")
print(emoji.emojize(test))
#print(emoji.demojize("🌏"))
