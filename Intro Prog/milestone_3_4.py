#Calculation Data
child_meal_cost=input("What is the cost of a children's meal? ")
adult_meal_cost=input("What is the cost of an adult meal? ")
count_children=input('How many children are in your party? ' )
count_adult=input('How many adults are in your party? ')
sales_tax=input('What is the sale tax rate at this store? ')

#subs total section maths 
child_total_cost=float(child_meal_cost)*float(count_children)
adult_total_cost=float(adult_meal_cost)*float(count_adult)
sub_total=(float(child_total_cost)+float(adult_total_cost))
print('Your Subtotal is:') 
print(f'${sub_total:.2f}')
print('Your Sales Tax is:')

#Sales Tax calculation
sales_tax_total=float(sub_total)*float(sales_tax)/100
print(f'${sales_tax_total:.2f}')

#total cost calculation
print('Your Total is:')
meal_total=(float(sales_tax_total)+float(sub_total))
print(f'${meal_total:.2f}')

#Payment input section
payment=input('Please insert payment amount: $')
change_remaining=float(payment) - (meal_total)
print(f'Here is your change: ${change_remaining:.2f} ')