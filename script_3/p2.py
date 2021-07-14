import math

class Circle:
    def __init__(self,rd):
        self.radius = rd

    def circumference_of_circle(self):
        return 2 * math.pi * self.radius
    
    def compare_circles():
        if no1>no2:
            print("Circle 1 is bigger than Circle 2")
        else:
            print("Circle 2 is bigger than Circle 1")

        
no1=int(input("Enter radius of circle 1 : "))
no2=int(input("Enter radius of circle 2 : "))

obj1 = Circle(no1)
obj2 = Circle(no2)

print(f"Circumference if circle 1: {obj1.circumference_of_circle()}")
print(f"Circumference if circle 2: {obj2.circumference_of_circle()}")

Circle.compare_circles()
