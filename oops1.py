# Initialize a class
class employee:
    # Special method/magic method/Dunder method
    def __init__(self):
        print("Started execting attributes")
        self.id = 1235
        self.salary = 50000
        self.designation = "SDE"
        print("completed execting attributes")

    def travel(self,destination):
        print("This travel function was called manuallay")
        print(f"Employee is now travelling to{destination}")      

# Creating an object of the class
sam = employee()

# Accessing the id attribute of the sam object
print(sam.id)
sam.travel("Kerala")
