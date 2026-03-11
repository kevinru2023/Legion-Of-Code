import sys
from classes.Planner import Planner
from classes.User import User
from classes.Viewer import Viewer


def main():
    print("Legion of Code - Workout Planner Application")
    print("============================================")
    
    username = input("Please Enter Your Username: ")
    email = input("Please Enter your email: ")
    
    user = User(username=username, email=email)
    user.save_credentials() # creates a creds file for user
    
    viewer = Viewer(user) 
    
    
    pass


if __name__ == "__main__":
    main()
