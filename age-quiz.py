'''
psuedocode:
get user to input age and store it in an interger varialble
if age is under 13 
out put message "You qualify for the kiddie discount"
if user is 21
output message"Congrats on your 21st"
if age is over 40 
output the message "Your over the hill"
if user is 65 or older 
output message "Enjoy your retirement"
The oldest someone can be is 100
if age is greater than 100 
output message "Sorry your dead"


for any other age
output message "Age is but a qtber'

'''

# ask user age and store in an interger variable
age = int(input('Age?'))

# check age conditions  and select output message using if, elif, else and boolean data type.
if age <13:
        print ('You qualify for the kiddie discount') 
elif age == 21:
        print('Congrats on your 21st')
elif age >100:
        print ('Sorry your dead')
elif age >= 65:
        print ('Enjoy your retirement')
elif age >40 :
        print('Your over the hill')

else:
        print ('Age is but a number')