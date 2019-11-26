menuList = []
priceList = []

def showBill():
    print("****** Chawapol's Shop ******")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
    print("*****************************")

def totalPrice():
    total = 0
    for number in range(len(menuList)):
        total += int(priceList[number])
    print("Total", total)

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Please Enter Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
totalPrice()
