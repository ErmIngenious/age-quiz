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
