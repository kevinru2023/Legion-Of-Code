"""
C-06: Viewer
Auth: Nolan Cutler
Supports EP-WOP-01, UR-IID-01, UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Planner[1]
"""

from classes.Planner import Planner
from classes.WorkoutPlan import WorkoutPlan
from classes.Session import Session
from models.Workout import Workout

from datetime import datetime

class Viewer:
    """
    This will probably exist in the frontend in some ohter language/framework; this
    "code" is just a tentative outline for the structure of how that class will be implemented.
    """

    def __init__(self, planner: Planner):
        self._planner: Planner = planner

    def create_plan(self) -> None:
        print("Creating new workout plan...")
        wpId = len(self._planner.list_plans())
        newWorkoutPlan = WorkoutPlan(id=wpId)
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            print(f"{day}:")
            name = input("\tExercise name: ")
            reps = int(input("\tReps: "))
            sets = int(input("\tSets: "))
            rest_time = int(input("\tRest time (seconds): "))
            video_id = input("\tVideo ID: ")
            wkt = Workout(name=name, reps=reps, sets=sets, rest_time=rest_time, video_id=video_id)
            newWorkoutPlan.add_workout(day, wkt)
        self._planner.add_plan(newWorkoutPlan)

    def view_plans(self) -> None:
        plans = self._planner.list_plans()
        if len(plans) == 0:
            print("No workout plans found.")
            return
        for plan in plans:
            print(f"Workout Plan {plan.id}:")
            for day, workouts in plan.workout_plan.items():
                for workout in workouts:
                    print(f"\t{day}: {workout.name} - {workout.reps} reps x {workout.sets} sets, rest {workout.rest_time}s")

    def log_workout(self) -> None:
        session = Session()
        today_name = datetime.today().strftime("%A")
        session.log_workout_day(today_name)
        session.track_id(len(self._planner.get_logs()))
        notes = input("Enter notes about today's workout: ")
        session.store_notes(notes)
        intensity = int(input("Enter perceived intensity (1-10): "))
        session.workout_intensity(intensity)
        # I have no clue why the hell the session has an associated workout, I feel like this can be correlated upstream
        self._planner.log_workout(session)

    def view_logs(self) -> None:
        logs = self._planner.get_logs()
        for log in logs:
            self._view_workout_session(log)

    def select_workout_plan(self) -> WorkoutPlan:
        plans = self._planner.list_plans()
        if len(plans) == 0:
            print("No workout plans found.")
            return None
        for plan in plans:
            print(f"Workout Plan {plan.id}:")
            for day, workouts in plan.workout_plan.items():
                for workout in workouts:
                    print(f"\t{day}: {workout.name} - {workout.reps} reps x {workout.sets} sets, rest {workout.rest_time}s")
        while True:
            plannerId = int(input("Enter the ID of the workout plan you want to select: "))
            for plan in plans:
                if plan.id == plannerId:
                    return plan
            print("Invalid ID, try again.")

    def _view_workout_session(self, session: Session) -> None:
        print(f"Session {session.id} on {session.day}:")
        print(f"\tNotes: {session.notes}")
        print(f"\tPerceived Intensity: {session.percieved_intensity}")
        if session.workout:
            print(f"\tWorkout: {session.workout.name} - {session.workout.reps} reps x {session.workout.sets} sets, rest {session.workout.rest_time}s")
