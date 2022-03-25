ticket_price = 5
food_prices = {"popcorn": 4, "soda": 2, "burger": 4.5}

def price_calculator(ticket_price,food_prices):
    
    total_charge = ticket_price
    
    print("Do you wanted to try our amazing food 😍😍 with great movies 🎥🎥🎬")
    user_input = input("Enter yes/no").lower()
    if user_input=="yes":
        print('\n')
        print("What you wanted to try ! We have following options ..!")
        
        print(f"{list(food_prices.keys())}")
        user_input_food = input("Enter food name please : ").lower()

        total_element_user_want = int(input("Please Enter Quantity"))
        price = food_prices.get(user_input_food)
        total_charge+=price*total_element_user_want
        print('')
        print("Do you want anything else : ")
        extra = input("Please Enter yes/no : ").lower()
    
        while extra=="yes":
            
            user_input_food = input("Enter food name please :").lower()
            total_element_user_want = int(input("Please Enter Quantity"))
            total_charge+=food_prices.get(user_input_food)*total_element_user_want
            print('')
            print("Do you want anything else : ")
            extra = input("Please Enter yes/no").lower()
            
        return total_charge
    else:
        return total_charge
    
print("How many ticket you want : ")
total_ticket = int(input("Enter ticket : "))
total_ticket_price =  total_ticket* ticket_price     
price_calculator(total_ticket_price,food_prices)     
