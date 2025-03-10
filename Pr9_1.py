# Write a Python program to create class KSV with attributes like class variable cnt, instance variables x and y, instance methods get_value and print_value

class KSV:
    cnt = 0  
    def __init__(self, x, y):
        self.x = x  
        self.y = y  
        KSV.cnt += 1  
    def get_value(self):
        return self.x, self.y 
    def print_value(self):
        print(f"x: {self.x}, y: {self.y}")  
    
obj1 = KSV(10, 20)
obj2 = KSV(30, 40)
obj1.print_value()  
obj2.print_value()  
print("Total instances created:", KSV.cnt)  