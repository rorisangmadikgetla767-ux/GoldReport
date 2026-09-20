import json
from Classes import XAUUSD
from os import path


def userInput():
    print("What influences Gold?")
    
    Influencer = input("Write your answers: (strictly 3 values..)  ")
    Pricing = float(input("What is the current price of Gold..? "))
    Director = input("What is the current direction of gold(Bullish/Bearish)? ")
    
    entry = XAUUSD(Influencer, Pricing, Director)
    
    
    
    with open("XAUUSD.txt", "a") as file:
        file.write(json.dumps(entry.to_dict()) + "\n")
            
            
        

print("==============")
print("Gold Tracker")
print("==============")

while True:
    try:
        menu = int(input("Enter a number: "))
        
        
    except ValueError:
        print("Please enter a number.")
        
        continue
    if menu == 1:
        userInput()
    else:
        print("The program is not yet finsihed .")
        exit()
        
    
    
    