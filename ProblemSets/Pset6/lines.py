import sys

if len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    try:
        file_name=sys.argv[1]
        if ".py" in file_name:
            with open(file_name,"r") as file:
                lines=file.readlines()
            no_of_lines=0
            for line in lines:
                if not line.lstrip().startswith("#") and not line.isspace():
                    no_of_lines+=1
            print(no_of_lines,end="")
            sys.exit()
        else:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")
