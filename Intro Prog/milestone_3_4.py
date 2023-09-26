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
print(sub_total)
print('Your Sales Tax is:')
sales_tax_total=float(sub_total)*float(sales_tax)/100
print(float(sales_tax_total))
print('Your Total is:')
print(float(sales_tax_total)+float(sub_total))