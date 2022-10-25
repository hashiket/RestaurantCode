import json


#We can get all the food items
with open("foodItem.txt", 'r') as file1:
            data = json.loads(file1.read())
#we can get all the  details of eater      
with open("Eater.txt", 'r') as file1:
            EaterData = json.loads(file1.read())
#we can get all the orders of restaurant
with open("ResLogFile.txt", 'r') as file1:
            LogData = json.loads(file1.read())




    
stl = 0  
while(stl!=1):

    dct = {}


    end = len(LogData)
    st=0
    count=0
    for key,value in LogData.items():
        second = value[0]
        item=value[1]
        for key,value in LogData.items():
            
            if value[0]==second and item==value[1]:
                count+=1
        if count>1:
            print("Got the error as eater_id found with same food")
            stl=1
            break
        count=0
    if stl==1:
        break
    for key,value in LogData.items():    
        if value[1] in dct:
            dct[value[1]] += 1
        else:
            dct[value[1]] = 1
    start=0
    print("!!!!!!!! Top 3 most famous Food Items are !!!!!!!!!")
    while(start!=3):
        Keymax = max(zip(dct.values(), dct.keys()))[1]
        start+=1
        print(str(start)+": "+data[str(Keymax)])
        dct.pop(Keymax)
                
    stl+=1

