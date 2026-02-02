"""
C-01: Class for Workout Plan 
Auth: Kevin Rubio, Aron Meraz 
Supports: EP-BRBS (have to rename later), (probalby supports other stuff)
Collaborators: ???
"""

class WorkoutPlan: 
    def __init__(self):
        self.workout_plan = {} # Init an empty dict for workout plan where Keys = Day of the week and Values = list of exercises
        self.last_rest_day = None # date of last rest day taken 
        self.current_streak = 0 # Days workouted in a row
    
    # Returns true if the workout plan is empty 
    def workout_plan_empty(self):
       return not self.workout_plan 
   
    # Will add a workout to the workout plan
    def add_workout(self, day, exercises): 
       return None 
    
    # Will calculate if a rest day is needed in the user's current workout plan 
    def calculate_rest_day(self): 
        return None
        