print("What is your favorite color?")
Color=input("Type Color Here:")
print("Your favorite color is:",Color)
if Color=='green': print ('Yes it is the best color.') 
if Color=='green':raise SystemExit
print("That is a silly color")
user_imput =input ('Do you want to know what the best color is? y/n')
if user_imput.lower ()== 'y':
    print('It is Green')
elif user_imput.lower() == 'n':print('Well only cool people get to know anyway.')
else: print('y or n')