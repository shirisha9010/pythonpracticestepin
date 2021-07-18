import Caluculate_Price
quantity = 0
next = True
weight = 0
cw = 0
total_weight = 0
Candy_Price = 0


 
def calculation(quantity,weight):
    totalbox_wt = 0
    total_candies = 0
    cw = weight * quantity
    cost = int(input())
    r = Caluculate_Price.price(cw, cost)
    totalbox_wt = totalbox_wt + cw
    total_candies = total_candies + quantity
    return cw,totalbox_wt,total_candies
    
def choices():
    print("Avaliable Candies")
    print("1. Mango Candy")
    print("2. Orange Candy")
    print("3. Strawberry Candy")
    print("4. Jellies")
    print("Choose an option 1-4")
    
def MangoCandy():
    print("Please enter the quantity of Mango Candy")
    quantity = int(input())
    print("Please enter the weight in grams of Mango Candy")
    weight = int(input())
    print("Enter price of Mango Candy")
    cw,totalbox_wt,total_candies = calculation(quantity,weight)
    print("The total weight of MangoCandy is: %d grams" %cw)
    print("The total weight of gift box is: %d" %totalbox_wt)
    print("Do you want any other item (y/n)")
    return totalbox_wt,total_candies

def OrangeCandy():
    print("Please enter the quantity of Orange Candy")
    quantity = int(input())
    print("Please enter the weight in grams of Orange Candy")
    weight = int(input())
    print("Enter price of Orange Candy")
    cw,totalbox_wt,total_candies = calculation(quantity,weight)
    print("The total weight of OrangeCandy is: %d grams" % cw)
    print("The total weight of gift box is: %d" % totalbox_wt)
    print("Do you want any other item (y/n)")
    return totalbox_wt,total_candies
    
def StrawberryCandy():
    print("Please enter the quantity of Strawberry Candy")
    quantity = int(input())
    print("Please enter the weight in grams of Strawberry Candy")
    weight = int(input())
    print("Enter price of Strawberry Candy")
    cw,totalbox_wt,total_candies = calculation(quantity,weight)
    print("The total weight of Strawberry Candy is: %d grams" % cw)
    print("The total weight of gift box is: %d" % totalbox_wt)
    print("Do you want any other item (y/n)")
    return totalbox_wt,total_candies
    
def result(totalbox_wt,total_candies):
    print("Total weight of gift box is: %d" %totalbox_wt)
    print("Total number of candies in the giftbox is: %d" %total_candies)
    
def Jellies():
    print("Please enter the quantity of Jellies")
    quantity = int(input())
    print("Please enter the weight in grams of Jellies")
    weight = int(input())
    print("Enter price of Jellies")
    cw,totalbox_wt,total_candies = calculation(quantity,weight)
    print("The total weight of Jellies is: %d grams" % cw)
    print("The total weight of gift box is: %d" % totalbox_wt)
    print("Do you want any other item (y/n)")
    return totalbox_wt,total_candies
    
    
def fun(next):
    print("What do you want for Gift Box Preparation ?")
    while next:
        choices()
        choice = int(input())
        if choice == 1:
            totalbox_wt,total_candies = MangoCandy()
            que = input()
            if(que == 'y'):
                next = True
            else:
                next = False
                result(totalbox_wt,total_candies)
                break
            
        elif choice == 2:
            totalbox_wt,total_candies = OrangeCandy()
            que = input()
            if (que == 'y'):
                next = True
            else:
                next = False
                result(totalbox_wt,total_candies)
                break
            
        elif choice == 3:
            totalbox_wt,total_candies = StrawberryCandy()
            que = input()
            if (que == 'y'):
                next = True
            else:
                next = False
                result(totalbox_wt,total_candies)
                break
            
        elif choice == 4:
            totalbox_wt,total_candies = Jellies()
            que = input()
            if (que == 'y'):
                next = True
            else:
                next = False
                result(totalbox_wt,total_candies)
                break

fun(next)