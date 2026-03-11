"""
C-01: Class for Workout Plan
Auth: Kevin Rubio, Aron Meraz
Supports: EP-BRBS, EP-WOP, UR-WP-01, UR-WP-02, UR-WP-03
Collaborators: Workout[0..7] (since there is 7 days in the week)
"""

from datetime import date
from models.Workout import Workout

class WorkoutPlan:
    def __init__(self, id: int):
        self.id: int = id
        self.workout_plan: dict[str, list[Workout]] = {}
        self.last_rest_day: str = None  # date of last rest day taken
        self.current_streak: int = 0  # Days workouted in a row

    def workout_plan_empty(self) -> bool:
        return not self.workout_plan

    def add_workout(self, day: str, workout: Workout) -> None:
        if day not in self.workout_plan:
            self.workout_plan[day] = []
        self.workout_plan[day].append(workout)

    def remove_workout(self, day: str) -> bool:
        if day in self.workout_plan:
            del self.workout_plan[day]
            return True
        return False

    def update_workout(self, day: str, workout: Workout) -> bool:
        if day in self.workout_plan:
            self.workout_plan[day] = [workout]
            return True
        return False
    
    def calculate_rest_day(self) -> str:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        today_name = date.today().strftime("%A")
        today_idx = days_of_week.index(today_name)
    
        # Find the next upcoming day (after today) not scheduled in the workout plan
        for i in range(1, 8):
            candidate = days_of_week[(today_idx + i) % 7]
            if candidate not in self.workout_plan:
                return candidate
    
        # All 7 days are planned — recommend rest based on streak-aware interval
        # Every 3 days if streak is high, every 4 if manageable
        rest_interval = 3 if self.current_streak >= 4 else 4
        return days_of_week[(today_idx + rest_interval) % 7]
