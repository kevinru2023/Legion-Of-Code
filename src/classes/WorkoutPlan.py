"""
C-01: Class for Workout Plan
Auth: Kevin Rubio, Aron Meraz
Supports: EP-BRBS, EP-WOP, UR-WP-01, UR-WP-02, UR-WP-03
Collaborators: Workout[0..7] (since there is 7 days in the week)
"""


class WorkoutPlan:
    def __init__(self):
        self._workout_plan = (
            {}
        )  # Init an empty dict for workout plan where Keys = Day of the week and Values = workout (probably will be class)

    # Returns true if the workout plan is empty
    def workout_plan_empty(self) -> bool:
        return not self._workout_plan

    # Will add a workout to the workout plan
    def add_workout(self, day, workout) -> None:
        return None

    # Will calculate if a rest day is needed in the user's current workout plan i.e. if they have 5 days in a row of working out
    def calculate_rest_day(self) -> bool:
        return False

    # Will calcuate which muslce groups are being undertrained or over trained in the current user's plan
    def calculate_muscle_group_balance(self) -> dict[str,int] | None:
        return None

    