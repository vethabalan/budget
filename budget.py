budget = int(input("enter a budget:"))  #assign a variable and enter the budget
def chennai(budget):                    #defining a function for chennai and input parameter
    onion = 30                              
    tomato = 15
    petrol_expense = 3/budget*budget                  # assign variables and giving them values and print it.
    print("nionnion",budget/onion)
    print("tomato",budget/tomato)
    print("petrol expense",petrol_expense)

    
    
def madurai(budget):                     #defining a function called madurai and input as budget
    onion = 34
    tomato = 10
    petrol_expense = 3/budget*budget                  # assign variables and giving them values and print it.
    print("onion",budget/onion)
    print("tomato",budget/tomato)
    print("petrol expense",petrol_expense)

    
    
def trichy(budget):                       #defining a function called trichy and input as budget
    onion = 27
    tomato = 45
    petrol_expense = 3/budget*budget                    # assign variables and giving them values and print it.
    print("onion",budget/onion)
    print("tomato",budget/tomato)
    print("petrol expense",petrol_expense)

print("chennai budget")                    #calling the functions
chennai(budget)
print("madurai budget")
madurai(budget)
print("trichy budget")
trichy(budget)

#def petrol(budget):
   # p = 3/budget*budget
   # print("petrol",p)
#print("petrol expense")
#petrol(budget)
