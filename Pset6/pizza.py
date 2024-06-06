import sys
from tabulate import tabulate
import csv

if len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    table=[]
    try:
        file_name=sys.argv[1]
        if ".csv" in file_name:
            with open(file_name) as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers="keys", tablefmt="grid"))
                sys.exit(0)
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")
