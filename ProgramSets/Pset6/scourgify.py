import sys
import csv

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    try:
        table=[]
        if ".csv" in sys.argv[1] and ".csv" in sys.argv[2] :
            with open(sys.argv[1],'r') as file:
                reader=csv.DictReader(file)
                for row in reader:
                    split_name=row["name"].split(",")
                    table.append({"first": split_name[1].lstrip(),"last":split_name[0],"house":row["house"]})

            with open(sys.argv[2],'w') as file1:
                writer=csv.DictWriter(file1,fieldnames=["first","last","house"])
                writer.writerow({"first":"first","last":"last","house":"house"})
                for row in table:
                    writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})

        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit(f"Could not read {file_name}")
