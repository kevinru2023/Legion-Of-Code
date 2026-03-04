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
        self._last_rest_day = None  # date of last rest day taken
        self._current_streak = 0  # Days workouted in a row

    # Returns true if the workout plan is empty
    def workout_plan_empty(self):
        return not self.workout_plan

    # Will add a workout to the workout plan
    def add_workout(self, day, workout):
        return None

    # Will calculate if a rest day is needed in the user's current workout plan
    def calculate_rest_day(self):
        return None

    # Will calcuate which muslce groups are being undertrained or over trained
    def calculate_muscle_group_balance(self) -> dict[str]:
        return None

    # Will return a dictionary mapping of muscle groups and their stats?
    # {
    #     Chest: frequency : 2, last worked: Friday, underworked: False, overworked: False
    #     Quads: frequency : 0, last worked: Monday, underworked: True, overworked: True
    # }


"""
C-02: Suggestion Engine
Auth: Kevin Rubio, Aron Meraz
Supports: EP-BRBS,  EP-WOP-01, UR-BRBS
Collaborators: Workoutplan
"""
class SuggestionEngine:
    # will generate suggestions by analyzing workout plans

    def __init__(self):
        # Empty for now
        pass

    def suggest_rest_day(self, workoutplan) -> str:
        # Will determin if rest is needed based on workout streak
        pass

    def suggest_muscle_group(self, workoutplan) -> str:
        # Will determine which muscle groups should be worked next based on their frequency and last day worked
        pass


"""
C-03: Workout
Auth: Nolan Cutler
Supports: EP-BRBS, UR-W0P-01
Collaborators: None
"""
@dataclass
class Workout:
    '''
    Stores information specific to an exercise
    '''
    self.name: str
    self.reps: int
    self.sets: int
    self.rest_time: int
    self.video_id: str

