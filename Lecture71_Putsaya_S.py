menuList = []
priceList = []
sum = 0

def showBill():
    print("--- MY FOOD ---")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    print("---------------")
    print("Total Price =",sum)
    print("---Thank You---")

while True:
    print("If you're finished Please type EXIT")
    menuName = input("Please enter menu : ")
    if menuName.lower() == "exit" :
        break
    else:
        menuPrice = int(input("Price : "))
        sum += menuPrice
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
