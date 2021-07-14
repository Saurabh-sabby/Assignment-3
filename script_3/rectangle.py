class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    
    def rectangle_area(self):
        return self.length*self.width
    

a=int(input("Enter length of rectangle: "))
b=int(input("Enter breath of rectangle: "))

newRectangle = Rectangle(a,b)
area=newRectangle.rectangle_area()
print(area)
        