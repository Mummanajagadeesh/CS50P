import requests
import sys

try:
    if(len(sys.argv))<2:
        print("Missing command-line argument")
        sys.exit(1)
    elif(sys.argv[1].isdigit==False):
        print("Command-line argument is not a number")
        sys.exit(1)
    else:
        value=float(sys.argv[1])
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r=(r.json())
        amount=(r['bpi']['USD']['rate_float'])*value
        print(f"${amount:,.4f}")

except requests.RequestException:
    pass
