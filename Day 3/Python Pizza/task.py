print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size=='S':
    price=15
elif size=='M':
    price=20
else:
    price=25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=='Y':
    if size =='S':
        price+=2
    else:
        price+=3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese =='Y':
    price+=1
print(f"Your final bill is: ${price}.")




