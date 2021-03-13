username = input("Username :")
password = input("Password :")

if username == "exercise8" and password == "8188216":

    print("Welcome to Example Shop\n")

    print("----------MENU------------")
    print("1.pepsi       15 THB/PIECE")
    pepsiPrice = int(15)
    print("2.rice         5 THB/PIECE")
    ricePrice = int(5)
    print("3.chocolate   25 THB/PIECE")
    chocolatePrice = int(25)
    print("4.book        50 THB/PIECE")
    bookPrice = int(50)
    print("5.water       15 THB/PIECE")
    waterPrice = int(15)
    print("--------------------------\n")

    print("What do you like to buy?")
    userSelected = int(input("Select number : "))

    if userSelected == 1:
        print("\nHow many do you want?")
        amount = int(input("Amount : "))
        pepsi = amount * pepsiPrice
        print("\nTotalPrice =",pepsi,"THB\n")
        print("Thank you\nHope to see you next time!")

    elif userSelected == 2:
        print("\nHow many do you want?")
        amount = int(input("Amount : "))
        rice = amount * ricePrice
        print("\nTotalPrice =",rice,"THB\n")
        print("Thank you\nHope to see you next time!")

    elif userSelected == 3:
        print("\nHow many do you want?")
        amount = int(input("Amount : "))
        chocolate = amount * chocolatePrice
        print("\nTotalPrice =",chocolate,"THB\n")
        print("Thank you\nHope to see you next time!")

    elif userSelected == 4:
        print("\nHow many do you want?")
        amount = int(input("Amount : "))
        book = amount * bookPrice
        print("\nTotalPrice =",book,"THB\n")
        print("Thank you\nHope to see you next time!")

    elif userSelected == 5:
        print("\nHow many do you want?")
        amount = int(input("Amount : "))
        water = amount * waterPrice
        print("\nTotalPrice =",water,"THB\n")
        print("Thank you :)\nHope to see you next time!")

    else:
        print("\nERROR\nPlease select number only in MENU!!!")

else:
    print("\nIncorrect!\nPlease try again")



