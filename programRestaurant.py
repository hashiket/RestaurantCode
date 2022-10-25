import json



with open("foodItem.txt", 'r') as file1:
            data = json.loads(file1.read())
        
with open("Eater.txt", 'r') as file1:
            EaterData = json.loads(file1.read())

with open("ResLogFile.txt", 'r') as file1:
            LogData = json.loads(file1.read())


start=1
while(start):
    print("!!!!!!!!WELCOME TO OUR RESTAURANT!!!!!!!!!!")
   
    print("1: Order Food")
    print("2: Get the top 3 food")
    print("3: Exit")


    choice  = int(input("Please enter your Choice :"))


    if choice==1:    
        print("List of Foods available..")
        for key,value in data.items():
            print(str(key)+": "+value)
        name=input("Enter our Name")
        food_choice = int(input("Enter your choice of food.."))
        Eln = len(EaterData)+1
        EaterData[Eln] = name
        with open("Eater.txt", 'w') as file1:
           file1.write(json.dumps(EaterData))

        LogData[len(LogData)+1] = [Eln,food_choice]
        with open("ResLogFile.txt", 'w') as file1:
           file1.write(json.dumps(LogData))

    elif choice==2:
        print("!!!!!!!! Top 3 most famous Food Items are !!!!!!!!!")
        dct = {}
        for key,value in LogData.items():

            if value[1] in dct:
                dct[value[1]] += 1
            else:
                dct[value[1]] = 1
        start=0
        while(start!=3):
            Keymax = max(zip(dct.values(), dct.keys()))[1]
            start+=1
            print(str(start)+": "+data[str(Keymax)])
            dct.pop(Keymax)
            

    elif choice==3:
        start=0
    

