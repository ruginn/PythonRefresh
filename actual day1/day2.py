print('Welcome to the tip calculator')
total = input('What was the total of the bill? \n $')
percent = input('What percent do you want to tip? 10, 15, 20%\n')
people = input('How many people where in your party? \n')

tipPerPerson = (float(total) * (int(percent) / 100)) / int(people)

print('Your tip amount is ' + str(tipPerPerson))


