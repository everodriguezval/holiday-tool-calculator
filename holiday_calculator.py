from sqlConnect import cursor

def search_country():
    global country
    country = input('Enter country you want to visit: ').title()
    country_quotes = "'" + country + "'"
    
    cursor.execute(f'SELECT * FROM holiday WHERE country = {country_quotes}')
    global data_row
    data_row = cursor.fetchall() # will return a tuple
    # print(data_row)
    if len(data_row) == 0:
        print('\nCountry not found in our database')
    else:
        print('\nCountry found in our database!')
        # for row in data_row:
        #     print(row)

print('\nWelcome to the holiday planning tool!\n')
print('To calculate how much money you will need for your trip, please answer the following questions:\n')
    
search_country()

number_of_people = int(input('\nHow many people travelling in your group? '))
number_of_days = int(input('\nNumber of days: '))

flight_cost_per_person = data_row[0][3]
total_flights = flight_cost_per_person * number_of_people

print('\nWhat is your budget? ')        
budget = int(input('\n1. Budget\n2. Medium\n3. Luxury\n\nEnter number: ')) 

if budget == 1:
    food = data_row[0][4]
    accommodation = data_row[0][7]
    activities = data_row[0][10]
    print('You chose option 1')

elif budget == 2:
    food = data_row[0][5]
    accommodation = data_row[0][8]
    activities = data_row[0][11]
    print('You chose option 2')

elif budget == 3:
    food = data_row[0][6]
    accommodation = data_row[0][9]
    activities = data_row[0][12]
    print('You chose option 3')

accomm_cost_all = (accommodation * (1.5**(number_of_people - 1))) * number_of_days
total_food = food * number_of_people * number_of_days
total_activities = activities * number_of_people * number_of_days
total_cost_all = total_flights + total_food + total_activities + accomm_cost_all
print(f'\nThe total price for {number_of_people} people for {number_of_days} days in {country} is £{total_cost_all}')


breakdown = input('\nDo you want to see the breakdown of the calculated cost per person? (Y/N): ').upper()
if breakdown == 'Y':
    total_cost_pp = total_cost_all / number_of_people
    flight_cost_pp = total_flights / number_of_people
    accomm_cost_pp = accomm_cost_all / number_of_people
    food_cost_pp =  total_food / number_of_people
    activities_cost_pp = total_activities / number_of_people
    
    print(f'\nBreakdown from £{total_cost_all}:\nCost per person:\n')
    print(f'Flights: £{flight_cost_pp}\nAccommodation: £{accomm_cost_pp}\nFood: £{food_cost_pp}\nActivities: £{activities_cost_pp}\n')
    print(f'Therefore, the total cost per person would be: £{total_cost_pp}\n')

else:
    print('Thanks for using the Holiday Calculator Application')
    exit
