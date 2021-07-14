class Greater:
    def __init__ (self, no1):
        self.no1 = no1 

    def __gt__(self, no2):
        if(self.no1 > no2.no1):
            return True
        else:
            return False

ob1 = Greater(20)
ob2 = Greater(15)

if(ob1>ob2):
    print("ob1 is greater than ob2") 
else:
    print("ob2 is greater than ob1")
