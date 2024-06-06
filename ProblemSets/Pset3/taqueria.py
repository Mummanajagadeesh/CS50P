menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
tot=0.0
while True:
	try:
		print("Item:",end="")
		item=input().title()
		tot+=float(menu[item])
		print(f"Total:${tot:.2f}")
	except EOFError:
		break
	except KeyError:
			continue
