class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_message(self):
        print(f"Hello {self.name} you are {self.age} years old! Welcome !!")


# The new user function asks user for input then creates a Person object
def new_user():

    try:
        # Ask for user's name then store it in a variable called user_name
        user_name = input("What is your fullname: ")

        # Ask for user's age then store it in a string variable called user_age
        user_age = int(input("What is your age: "))

        new_person = Person(user_name, user_age)
        return new_person.print_message()
    except ValueError:
        print("Error - please enter a number")


user = new_user()
