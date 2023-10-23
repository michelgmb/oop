# Create a class named User
class User:
    # Add an __init__ method to the User class. The init method to have \
    # three parameters, self, name, and birthyear.
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear


    # have two methods get_name and age
    # the 2 method should contains pass statement only

    def get_name(self):
        # method to contain only pass statement  in them
        # method should have only one parameter self
        pass

    def age(self, current_year):
        # method should have only 2 parameters self ,current_year
        # method to contain only pass statement  in them
        age = current_year - self.birthyear
        return age


"""Implement/code the User.age method so the method returns the age of the user given 
the self.birthyear instance variable and the current_year parameters."""
user = User('jonh', 1982)
print(user)
print(user.age(2023))


