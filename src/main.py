import sys
from classes.Planner import Planner
from classes.User import User
from classes.Viewer import Viewer
from classes.SuggestionEngine import SuggestionEngine


def main():
    print("Legion of Code - Workout Planner Application")
    print("============================================")

    username = input("Please Enter Your Username: ")
    email = input("Please Enter your email: ")

    user = User(username=username, email=email)
    user.save_credentials()  # creates a creds file for user

    viewer = Viewer(user)

    while True:
        print("\nMenu:")
        print("1. Create Workout Plan")
        print("2. View Workout Plans")
        print("3. Edit Workout Plan")
        print("4. Add Workout Log")
        print("5. View Workout Logs")
        print("6. Get a Suggestion")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            viewer.create_plan()
        elif choice == "2":
            viewer.view_plans()
        elif choice == "3":
            viewer.edit_plan()
        elif choice == "4":
            viewer.log_workout()
        elif choice == "5":
            viewer.view_logs()
        elif choice == "6":
            engine = SuggestionEngine()
            plans = viewer._planner.list_plans()
            if plans:
                print(engine.suggest_rest_day(plans[0]))
            else:
                print("No workout plan found.")
        elif choice == "7":
            print("Exiting application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
