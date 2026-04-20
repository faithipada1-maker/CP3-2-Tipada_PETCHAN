userName = input("Username :")
password = input("Password:")
if userName == "Tipada" and password == "fai123":
    print("DONE!")
    print("---SHOP---")
    print("1.milk 20 BAHT")
    print("2.bread 15 BAHT")
    print("3.Yogurt 12 BAHT")
    userSelect1 = int(input("How manybox of milk do you want : "))
    userSelect2 = int(input("How many bread do you want :"))
    userSelect3 = int(input("How many yogurt do you want :"))
    result = (userSelect1*20) + (userSelect2*15) + (userSelect3 *12)
    print(result,"Baht")
elif userName != "Tipada" or password !=  "fai123":
    print("ERROR!")
    print("Please try again")





