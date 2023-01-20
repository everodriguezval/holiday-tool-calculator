from sqlConnect import cursor

def holiday_calculator():
    def search_country():
        print('\nWelcome to the holiday planning tool!\U0001F30D\n\n')
        print('To calculate how much money you will need for your trip, please answer the following questions:\n')
        global country

        no_country_found = True
        while no_country_found:
            country = input('Enter country you want to visit: ').title()
            country_quotes = "'" + country + "'"
        
            cursor.execute(f'SELECT * FROM holiday WHERE country = {country_quotes}')        
            data_row = cursor.fetchall() # will return a tuple
            # print(data_row)
            if len(data_row) == 0:
                print('\nCountry not found in our database\nPlease, try again\n')

            else:
                print('\nGreat news. Country found in our database!')
                no_country_found = False 
        return data_row    
    
    def valid_integer():
        not_valid = True
        while not_valid:
            try:                
                number = int(input())
                if number > 0:
                    not_valid = False
                else:
                    print('Number of people must be greater than 0')
            except ValueError:
                print("You must enter a whole number")
        return number

    destination = search_country()

    def valid_integer2():
        not_valid2 = True
        while not_valid2:
            budget_input = int(input())
            if budget_input == 1 or budget_input == 2 or budget_input == 3:
                not_valid2 = False
            else:
                print('Invalid number. Please enter 1, 2 or 3')
        return budget_input

    def budget(budget):
        if budget == 1:
            food = destination[0][4]
            accommodation = destination[0][7]
            activities = destination[0][10]
            print('You chose option 1')

        elif budget == 2:
            food = destination[0][5]
            accommodation = destination[0][8]
            activities = destination[0][11]
            print('You chose option 2')

        elif budget == 3:
            food = destination[0][6]
            accommodation = destination[0][9]
            activities = destination[0][12]
            print('You chose option 3')

        # we considered that accommodation increases by (1.5**(number_of_people - 1)) per extra person
        total_accommodation = (accommodation * (1.5**(number_of_people - 1))) * number_of_days
        total_food = food * number_of_people * number_of_days
        total_activities = activities * number_of_people * number_of_days
        total_cost_all = total_flights + total_food + total_activities + total_accommodation

        return total_accommodation, total_food, total_activities, total_cost_all   

    def breakdown():
            total_cost_pp = total_cost_per_item[3] / number_of_people
            flight_cost_pp = total_flights / number_of_people
            accomm_cost_pp = total_cost_per_item[0] / number_of_people
            food_cost_pp =  total_cost_per_item[1] / number_of_people
            activities_cost_pp = total_cost_per_item[2] / number_of_people
            
            return total_cost_pp, flight_cost_pp, accomm_cost_pp, food_cost_pp, activities_cost_pp


    print('\nHow many people travelling in your group?')
    number_of_people = valid_integer()
    print('\nEnter number of days:')
    number_of_days = valid_integer()
    flight_cost_per_person = destination[0][3]
    total_flights = flight_cost_per_person * number_of_people

    print('\nWhat is your budget? ')
    print('\n1. Budget\n2. Medium\n3. Luxury\n\nEnter number:')         
    budget_validated_input = valid_integer2()
    total_cost_per_item = budget(budget_validated_input)

    print(f'\nThe total price for {number_of_people} people for {number_of_days} days in {country} is £{total_cost_per_item[3]:.2f}')
    print(f'\nDo you want to see the breakdown of the calculated cost per person? (Y/N):')

    breakdown_input = input().upper()

    if breakdown_input == 'Y':
        total_cost_per_person = breakdown()
        print(f'\nBreakdown from £{total_cost_per_item[3]:.2f}:\nCost per person:\n')
        print(f'Flights: £{total_cost_per_person[1]:.2f}\nAccommodation: £{total_cost_per_person[2]:.2f}\nFood: £{total_cost_per_person[3]:.2f}\nActivities: £{total_cost_per_person[4]:.2f}\n')
        print(f'Therefore, the total cost per person will be: £{total_cost_per_person[0]:.2f}\n')   
    else:
        print('Thanks for using this holiday calculator application\n')


holiday_calculator()

another_search = True
while another_search:
    print(f'Do you want to do another search? (Y/N): ')
    new_search = input().upper()
    if new_search == 'Y':
        holiday_calculator()
    else:
        print(f'Thanks for using our application \U0001f600')
        another_search = False