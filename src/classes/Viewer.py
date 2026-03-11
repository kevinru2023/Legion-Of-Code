"""
C-06: Viewer
Auth: Nolan Cutler
Supports EP-WOP-01, UR-IID-01, UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Planner[1]
"""

from .Planner import Planner
from .Session import Session
from .WorkoutPlan import WorkoutPlan
from models.Workout import Workout

ALLOWED_WEEKDAYS = {"sun", "mon", "tues", "wed", "thurs", "fri", "sat"}


class Viewer:
    """
    Manages workout plans/logs through CLI menu
    """

    def __init__(self, user=None):
        self.set_user(user)

    def create_plan(self) -> None:
        plan = self._create_plan_cli()

        if plan is None:
            return

        self._planner.add_plan(plan)

    def view_plans(self) -> None:
        plans = self._planner.list_plans()
        self._view_plans_cli(plans)

    def log_workout(self) -> None:
        session = self._log_workout_cli()

        if session is None:
            return

        self._planner.log_workout(session)

    def view_logs(self) -> None:
        self._logs_cli(self._planner.get_logs())

    def select_workout_plan(self) -> WorkoutPlan | None:
        plans = self._planner.list_plans()
        return self._select_plan_cli(plans)

    def edit_plan(self) -> None:
        plan = self.select_workout_plan()
        if plan is None:
            print("No plan selected")
            return

        self._edit_plan_cli(plan)
        self._planner.save_plans()

    def set_user(self, user) -> None:
        if not user:
            raise ValueError("No user cannot initialize Viewer")
        self._user = user
        self._planner = Planner(user) # Critical for the entire app lol

    def _view_workout_session(self, session: Session) -> None:
        day = session.day
        notes = session.notes

        try:
            workout = session.workout
        except Exception as e:
            workout = None

        intensity = session._perceived_intensity
        print(f"Day: {day}, Workout: {workout}, Intensity: {intensity}, Notes: {notes}")

    def _logs_cli(self, logs: list[Session] = []) -> None:
        if not logs:
            print("No workout logs")
            return

        # print workout logs
        # e.g 1. ID: 1, Day: Wednesday
        #     2. ID: 2, Day: Thursday
        print("Workout logs:")
        for index, session in enumerate(logs, start=1):
            print(f"{index}. ID: {session.id}, Day: {session.day}, Notes: {session.notes}, RPE: {session._perceived_intensity}, Workout: {session.workout}") # this could break in the future since workout can be null


    def _select_plan_cli(self, plans=None) -> WorkoutPlan | None:
        if not plans:
            return None

        print("Select workout plan:")
        for index, plan in enumerate(plans, start=1):
            # get workout plan keys (days of week)
            days = list(plan.workout_plan.keys())
            print(f"{index}. Days: {days}")

        # index into days to select plan
        raw = input("Enter number: ").strip()
        if raw.isdigit():
            selected = int(raw)
            if 1 <= selected <= len(plans):
                return plans[selected - 1]
            else:
                print("Invalid selection")

        return None

    def _view_plans_cli(self, plans=None) -> None:
        if not plans:
            print("No saved workout plans")
            return

        print("Saved workout plans:")
        # list out workouts
        for index, plan in enumerate(plans, start=1):
            data = plan.workout_plan
            print(f"{index}. {data}")

    def _log_workout_cli(self) -> Session | None:
        day = self._prompt_weekday("Workout day (sun/mon/tues/wed/thurs/fri/sat): ")
        if day is None:
            return None

        notes = input("Notes: ").strip()
        intensity = self._input_int("Perceived intensity 1-10: ")

        id = len(self._planner.get_logs()) + 1

        # Need to add workout logging to the CLI and link it to th session 
        # will create an additiona cli function to input workout details and return a workout obj
        
        w = self._input_exercise()
        session = Session(id = id, day=day, notes=notes, perceived_intensity=intensity, workout=w, date=None, duration_minutes=0)
        return session

    def _create_plan_cli(self) -> WorkoutPlan:
        plan = WorkoutPlan()

        print("Create plan. Leave weekday empty to finish")
        while True:
            day = self._prompt_weekday("Day (sun/mon/tues/wed/thurs/fri/sat): ", allow_empty=True)
            if day is None:
                break

            exercise = self._input_exercise()
            if exercise is None:
                continue

            if day not in plan._workout_plan:
                plan._workout_plan[day] = []

            plan._workout_plan[day].append(exercise)

        return plan

    def _edit_plan_cli(self, plan: WorkoutPlan):
        print("Current plan:")
        print(plan._workout_plan)

        day = self._prompt_weekday("Day to edit (sun/mon/tues/wed/thurs/fri/sat): ")
        action = input("Type 'remove' to remove day, otherwise press Enter to replace workouts: ").strip().lower()

        if action == "remove":
            if day in plan._workout_plan:
                del plan._workout_plan[day]
                print("Day removed")
            else:
                print("Day not found in plan")
            return

        exercise = self._input_exercise()
        if exercise is None:
            print("No changes made")
            return

        plan._workout_plan[day] = [exercise]
        print("Plan updated")

    def _input_int(self, prompt: str, default: int = 0) -> int:
        raw = input(prompt).strip()
        if raw.isdigit():
            return int(raw)
        return default

    def _input_exercise(self) -> Workout | None:
        name = input("Workout name: ").strip()
        if name == "":
            return None

        reps = self._input_int("Reps: ", default=0)
        sets = self._input_int("Sets: ", default=0)
        rest_time = self._input_int("Rest time (seconds): ", default=0)
        video_id = input("Video id: ").strip()

        return Workout(
            name=name,
            reps=reps,
            sets=sets,
            rest_time=rest_time,
            video_id=video_id,
        )

    def _prompt_weekday(self, prompt: str, allow_empty: bool = False) -> str | None:
        while True:
            day = input(prompt).strip().lower()

            if day == "" and allow_empty:
                return None

            if day in ALLOWED_WEEKDAYS:
                return day

            print("Invalid weekday. Use: sun, mon, tues, wed, thurs, fri, sat")

