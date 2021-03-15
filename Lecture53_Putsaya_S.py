def vatCalculator():
    totalPrice = int(input("Total Price : "))
    result = totalPrice + (totalPrice * 7/100)
    return "Total Price + VAT = " + str(result) +" THB"
print(vatCalculator())