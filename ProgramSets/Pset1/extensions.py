test=input("File name: ")
test=test.lower().strip()
format=test[test.rfind(".")+1:]
if format=="gif":
    print(f"image/{format}")
elif format=="jpg":
    print(f"image/jpeg")
elif format=="jpeg":
    print(f"image/jpeg")
elif format=="png":
    print(f"image/{format}")
elif format=="txt":
    name=test[:test.find(".")]
    print(f"text/{name}")
elif format=="zip":
    print(f"application/{format}")
elif format=="bin":
    print("application/octet-stream")
elif test.find('.')==-1:
    print("application/octet-stream")
elif format.lower()=="pdf" or test.lfind(".")!=test.rfind("."):
    print(f"application/{format}")
