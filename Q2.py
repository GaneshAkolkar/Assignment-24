class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. My email is {self.email}.")
