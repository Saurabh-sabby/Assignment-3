class Circle:
    def __init__(self,no1,no2):
        self.input1 = no1
        self.input2 = no2

    def area(no1,no2):
        if no1 ==no2 :
            print("True")
        else:
            print("false")


no1 = input("Enter Radius of Circle 1:")
no2 = input("Enter Radius of Circle 2:")


print(Circle.area(no1,no2))



