print("Welcome to the Shopping Cart Program!")
cart = []
prices = []

while True:
print()
print("Please select an option:")
print("1. Add item")
print("2. View cart")
print("3. Remove item")
print("4. Compute total")
print("5. Exit")

select = int(input("Type in a number to continue: "))

if select == 1:
item = input("What would you like to add? ")
price = float(input("Type in the price: "))
cart.append(item)
prices.append(price)
print(f"'{item}' has been added to your cart.")
print(f"The price is ${price}")

elif select == 2:
print("This is what is in your shopping cart:")
for i in range(len(cart)):
print(f"{cart[i]} - ${prices[i]}")
input("Press Enter to continue")

elif select == 3:
takeout = input("Type in what you would like to remove: ")
if takeout in cart:
index = cart.index(takeout)
cart.pop(index)
prices.pop(index)
print(f"'{takeout}' has been removed from your cart.")
else:
print(f"'{takeout}' is not in your cart.")

elif select == 4:
if len(cart) == 0:
print("Your cart is empty.")
else:
total_price = sum(prices)
print(f"Total price: ${total_price:.2f}")
input("Press Enter to continue")

elif select == 5:
print("Thank you for shopping with us!")
break

else:
print("Invalid option. Please select a valid option.")
`