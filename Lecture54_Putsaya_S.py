def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "54" and passwordInput == "5420":
        return showMenu()
    else:
        return ("Incorrect"+"\nPlease Try Again!")

def showMenu():
    print("--Welcome to Shop--")
    print("1. Vat Calculate")
    print("2. Price Calculate")
    print("-------------------")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculate(int(input("Total Price : ")))

    elif userSelected == 2:
        return priceCalculate()
    else:
        return ("Not Available in Menu"+"\nPlease Try Again!")

def vatCalculate(totalPrice):
    vat = 7 / 100
    result = totalPrice + (totalPrice * vat)
    return ("Total Price + VAT = "+str(result)+" THB"+"\n---THANK YOU---")

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1+price2)

print(login())

