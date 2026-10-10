def display_welcome():
    print("Welcome to Where Do I go on Holiday Planner!")
    print("This program will help you decide where to go on holiday based on some questions you will be asked")
display_welcome()

name=str(input("Please enter your name: "))
age=int(input("Please enter your age: "))

def age_validation(age):
    if age < 18:
        print("Sorry, you are not old enough to go on holiday alone.")
        return False
    else:
        print("You are old enough to go on holiday.We will proceed with further questions.")
        return True

age_validation(age)


budget=float(input("Please enter your budget in EUR: "))
weather=str((input("What type of weather do you prefer for your holiday?sunny or cold: ")).lower())
location=str((input("What type of location do you prefer for your holiday?beaches or mountains: ")).lower())
local=str((input("Do you prefer to stay in your local area or travel abroad?local or abroad: ")).lower())
days=int(input("How many days do you want to go on holiday for? "))


def time_validation(days):
    if days < 3:
        return False
    else:
        return True

time_validation(days)



def budgetandtime_validation(budget,time_validation):
    if budget < 1000.00 :
        print("You do not have sufficient funds for a holiday abroad.We will attempt to find a local holiday destination based on your preferences.")
        return False

    elif budget >1000.00 and time_validation is False:
        print("You have sufficient funds for a holiday abroad but you do not have enough time to go on holiday abroad.We will attempt to find a local holiday destination based on your preferences.")
        return True
    else: 
        print("You have sufficient budget for a local or abroad holiday destination.We will attempt to find a holiday destination based on your preferences.")
        return True

budgetandtime_validation(budget, time_validation(days))

age_ok=age_validation(age)
budget_ok=budgetandtime_validation(budget, time_validation(days))



def holiday_recommendation(weather,location,local,age_ok,budget_ok):
    
    
    if age_ok is True and budget_ok is True:

        if weather == "sunny" and location == "beaches":
            recommendation= "Based on your preferences, we recommend you to go to the Canary Islands for a leisurely beach holiday."
            return recommendation       
        elif weather == "sunny" and location == "mountains":
            recommendation= "Based on your preferences, we recommend you to go to the Atlas mountains in Moroccofor a hiking holiday."
            return recommendation
        elif weather == "cold" and location == "beaches":
            recommendation= "Based on your preferences, we recommend you to go to the Faroe Island for an arctic getaway holiday."
            return recommendation
        elif weather == "cold" and location == "mountains":
            recommendation= "Based on your preferences, we recommend you to go to the Austrian Alpsfor a winter mountain holiday."
            return recommendation
        #else:
            #recommendation= "Based on your preferences, we are unable to provide a recommendation at this time"
            #return recommendation   

    elif age_ok is True and budget_ok is False:
        if weather == "sunny" and location == "beaches":
            recommendation= "Based on your preferences, we recommend you to go to Kilkee for a leisurely beach holiday."
            return recommendation
        elif weather == "sunny" and location == "mountains":
            recommendation= "Based on your preferences, we recommend you to go to the Wicklow mountains for a hiking holiday."
            return recommendation   
        elif weather == "cold" and location == "beaches":
            recommendation= "Based on your preferences, we recommend you to explore the beaches of County Donegal for a cold beach holiday."
            return recommendation
        elif weather == "cold" and location == "mountains":
            recommendation= "Based on your preferences, we recommend you to go to the mountains in Switzerland for a winter mountain holiday."
            return recommendation
        #else:
        
          #recommendation= "Based on your preferences, we are unable to provide a recommendation at this time"
          #return recommendation
    else:
        recommendation= "Based on your preferences, we are unable to provide a recommendation at this time due to your selected preferences"
        return recommendation

print(holiday_recommendation(weather,location,local,age_ok,budget_ok))

