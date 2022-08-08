budget = int(input("enter a budget:"))  #assign a variable and enter the budget
def chennai(budget):                    #defining a function for chennai and input parameter
    o = 30                              
    t = 15
    p = 3/budget*budget                  # assign variables and giving them values and print it.
    print("onion",budget/o)
    print("tomato",budget/t)
    print("petrol expense",p)

    
    
def madurai(budget):                     #defining a function called madurai and input as budget
    o = 34
    t = 10
    p = 3/budget*budget                  # assign variables and giving them values and print it.
    print("onion",budget/o)
    print("tomato",budget/t)
    print("petrol expense",p)

    
    
def trichy(budget):                       #defining a function called trichy and input as budget
    o = 27
    t = 45
    p = 3/budget*budget                    # assign variables and giving them values and print it.
    print("onion",budget/o)
    print("tomato",budget/t)
    print("petrol expense",p)

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
