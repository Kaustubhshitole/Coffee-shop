MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "cofee":18,
            
        },
        "cost":1.5,
        
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "cofee":24,

        },
        "cost":2.5,

    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "cofee":24,
        },
        "cost":3.0,
    }
}

profit =0
resources={
    "water":300,
    "milk":200,
    "cofee":100,
    }


#TODO: 3. Create function that will print out main message "What would you like?"(espresso/latte/cappuccino)
def menuSelection():
    userSelection =""
    userSelection.lower()

#TODO : 1. Create a while loop that will execute while a cofee machine is 'on'
    while (userSelection !="off"):
        userSelection= input("What would you like? (espresso/latte/cappuccion)\n")

#TODO: 2.print a report of all the cofee resources 
        if(userSelection =="report"):
            for element in resources:
                print(element + ":"+str(resources[element]))
                print(f"profit:0 ${profit}")
        elif(userSelection=="espresso"):
            if (checkResources("espresso")==True):
              checkout("espresso")  
            if (checkResources("latte")==True):
              generateEspresso()

        else:
         print("I am so sorry! I don't think we actually have that drink :(") 


        def checkout(drink):
          global profit

        costOfDrink =(MENU[drink]["cost"])
        currentAmount =0
        Coins ={'Quarters':.25,'dimes': .10,'Nickles': .05,'pennies': .01} 

        print("Nice,"+drink+"is my personal favorite!!"+"That will be :$"+str(costOfDrink))


        for element in Coins:
         userInput = input(f"How many {element} would you like to use ( use integers)?")
        currentAmount= int(userInput) * Coins.get(element) 
        print("Remaining total:"+ str(costOfDrink-currentAmount)) 



        if currentAmount<costOfDrink:
         print("I am so sorry! It appars you are "+ str(costOfDrink)+"short")
        else:
         if currentAmount>costOfDrink:
          print("Yea!! Here is your change  $"+str(costOfDrink * -1))

        print("Enjoy!!")
        profit +=(MENU[drink]["cost"])


        #TODO: 4. check resources to seeif you have enough to make drinks
        def checkResources(drink):

        #==========================================================================
        # Acquire the amount of resources that will
        # remain once the current drinks requirements
        # have been deducted. This will aid in determining
        # if we have enough to make the drink
        #=======================================================================

         futureWater = resources["water"]- MENU[drink]["ingredients"]["water"]
        futurecoffeeAmount = resources["cofee"]-MENU[drink]["ingredients"]["cofee"]
        depleteResources =" "

        if(drink !="espresso"):
         futureMilkAmount = resources["milk"]-MENU[drink]["ingredients"]["milk"]
        else:
        
        #==========================================================================
        #Identify what resoureces are depleted and prompt user
        #=========================================================================
         if futureMilkAmount <=0:
           depleteResources="Cofee"
        if futureMilkAmount <=0:
         if depleteResources !="":
          depleteResources +=",water"
        else:
         depleteResources +="Water"
        if futureMilkAmount and drink !="espresso" <=0:
         if depletedResources != "":
           depletedResources +="Milk"
        if depletedResources !="":
          print("I am so sorry! It appears we are low on"+depletedResources)
        return False

        #=========================================================================
        # Deduct the resources used to make cofee
        #=========================================================================

        resources["water"] -=MENU[drink]["ingredients"]["Water"]
        resources["cofee"] -=MENU[drink]["ingredients"]["cofee"]

        if drink !="espresso":
         resources["milk"] -=MENU[drink]["ingredients"]["milk"]


        return True


        #==========================================================================
        #kick off program
        #=========================================================================

        print("Let's Rock!")
        menuSelection()
            