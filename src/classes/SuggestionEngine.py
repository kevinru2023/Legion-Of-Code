"""
C-02: Suggestion Engine
Auth: Kevin Rubio, Aron Meraz
Supports: EP-BRBS, EP-WOP-01, UR-BRBS
Collaborators: WorkoutPlan
"""

from Planner import Planner
from WorkoutPlan import WorkoutPlan

from datetime import date

class SuggestionEngine:
    def suggest_rest_day(self, workoutplan: WorkoutPlan) -> str:
        restday = workoutplan.calculate_rest_day()
        today_name = date.today().strftime("%A")
        if restday == today_name:
            return "Today is a good day to rest!"
        return f"Consider taking a rest day on {restday}."

    def suggest_muscle_group(self, workoutplan: WorkoutPlan) -> str:
        
        pass
