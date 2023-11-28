
height_check_1 = int(input('tell me your height in inches'))
if height_check_1 > 36:
    passnger_check = int(input('How many riders are there?'))
    if passnger_check == 1:
        age_check_one= int(input('What is your age?'))
        if age_check_one >17 and height_check_1>61:
            print(' By the power invested in me as a underpaid ammusmant park employee you may ride this ride. You are welcome')
        else:
            print('You suck you are too small')
    if passnger_check==2:
        height_check_2=int(input('Please tell me the second paswagers height'))
        age_check_two=int(input('What is your age?'))
        if age_check_one or age_check_two >18:
           print(' By the power invested in me as a underpaid ammusmant park employee you may ride this ride. You are welcome')
        else:
            print('No you are ban.')
    else:
        print('That is not a valid option')
   
