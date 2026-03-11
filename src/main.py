from classes.User import User
from classes.Viewer import Viewer
from classes.ProgressAnalyzer import ProgressAnalyzer

def print_menu():
    print("\n=== Legion of Code ===")
    print("1. Start a new workout")
    print("2. View saved workout plans")
    print("3. Create a new workout plan")
    print("4. Log today's workout")
    print("5. View workout logs")
    print("6. View progress stats")
    print("7. View profile")
    print("0. Exit")
    print("======================")

def main():
    username = input("Enter your username: ").strip()
    user = User(username)
    info = user.get_user_info()
    print(f"\nWelcome, {info['name']}!")

    viewer = Viewer(user.get_planner())

    while True:
        print_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            plan = viewer.select_workout_plan()
            if plan:
                print(f"\nStarting workout plan {plan.id}...")
                viewer.log_workout()

        elif choice == "2":
            viewer.view_plans()

        elif choice == "3":
            viewer.create_plan()
            print("Workout plan created!")

        elif choice == "4":
            viewer.log_workout()

        elif choice == "5":
            viewer.view_logs()

        elif choice == "6":
            sessions = user.get_sessions()
            if not sessions:
                print("No sessions logged yet.")
            else:
                analyzer = ProgressAnalyzer(sessions)
                report = analyzer.generate_report()
                print("\n=== Progress Report ===")
                for key, value in report.items():
                    print(f"  {key}: {value}")

        elif choice == "7":
            for key, value in user.get_user_info().items():
                print(f"  {key}: {value}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()