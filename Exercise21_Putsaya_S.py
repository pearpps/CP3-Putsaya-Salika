from tkinter import *
import math

def leftClickButton(event):
    result = float(textboxWeight.get()) / math.pow(float(textboxHeight.get()) / 100, 2)
    print(result)
    labelResult.configure(text = result)

    if (result >= 30.0):
        labelDescribe.configure(text = "อ้วนมาก")

    elif (result >= 25.0 and result <= 29.9):
        labelDescribe.configure(text = "อ้วน")

    elif (result >= 23 and result <= 24.9):
        labelDescribe.configure(text = "น้ำหนักเกิน")

    elif (result >= 18.6 and result <= 22.9):
        labelDescribe.configure(text = "น้ำหนักปกติ เหมาะสม")

    else:
        labelDescribe.configure(text = "ผอมเกินไป")


mainWindow = Tk()
labelHeight = Label(mainWindow,text = "ส่วนสูง (cm.)")
labelHeight.grid(row = 0,column = 0)
textboxHeight = Entry(mainWindow)
textboxHeight.grid(row = 0,column = 1)
labelWeight = Label(mainWindow,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row = 1,column = 0)
textboxWeight = Entry(mainWindow)
textboxWeight.grid(row = 1,column = 1)
calculateButton = Button(mainWindow,text ="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row = 2,column = 0)
labelResult = Label(mainWindow,text = "ค่า BMI")
labelResult.grid(row = 2,column = 1)
labelDescribe = Label(mainWindow,text = "เกณฑ์ BMI",fg = "white",bg = "green",font = ("Helvetica",15))
labelDescribe.grid(row = 3,column = 1)

mainWindow.mainloop()