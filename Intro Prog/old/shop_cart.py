#Greeting
print('Welcome! To the Shopping Cart dooodad!')
#variable list hold
cart= []
costs=[]

#interface nightmare!
while True:
    print('----------------------------------------------')
    print('Please Select one of the bellow options! ')
    print('1. Add item to the cart')
    print('2.View cart contents')
    print('3.Remove item from the cart')
    print('4.Calculate total Cost!')
    print('5. Close out the program!')

    select=int(input('PLEASE TYPE A NUMBER TO CONTINUE!: '))

    if select== 1:
        item=input("What would you like to add to your cart? ")
        cost= float(input('What is the price?'))
        cart.append(item)
        costs.append(cost)
        print(f"'{item}' is now in your cart.")
        print(f"The price is ${cost}")
    elif select==2:
        print('this is what is in your shopping cart right now!')
        for i in range(len(cart)):
            print(f"{cart[i]} - ${costs[i]}")
        input("Press Enter to continue")
    elif select==3:
        takeout=input('Type in the item you want removed from your cart!')
        if takeout in cart:
            index=cart.index(takeout)
            cart.pop(index)
            costs.pop(index)
            print(f"'{takeout}' has been removed from your shopping cart!")
        else:
            print(f"'{takeout}' is not in your cart!")
    elif select==4:
        if len(cart)==0:
            print('Your cart is empty!')
        else:
            total_price=sum(costs)
            print(f"Total Price:${total_price:.2f}")
    elif select==5:
        print('Thanks for Shopping with us!')
        break
else:
    print('Please eneter a valid number!')