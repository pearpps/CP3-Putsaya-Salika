systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ผสม":50,"ข้าวมันไก่พิเศษ":45}
menuList = []

def showBill():
    print("--------------MY FOOD-------------")
    sum = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        sum += (menuList[number][1])
    print("----------------------------------")
    print("Total =",sum)

while True:
    menuName = input("Menu Selected :")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()



