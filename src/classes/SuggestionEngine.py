"""
C-02: Suggestion Engine
Auth: Kevin Rubio, Aron Meraz
Supports: EP-BRBS, EP-WOP-01, UR-BRBS
Collaborators: WorkoutPlan
"""


class SuggestionEngine:
    # will generate suggestions by analyzing workout plans

    def __init__(self):
        # Empty for now
        pass

    def suggest_rest_day(self, workoutplan) -> str:
        if workoutplan.calculate_rest_day():
            return "You have 5+ consecutive workout days. Consider adding a rest day."
        return "Your workout looks balanced. No rest needed."

    def suggest_muscle_group(self, workoutplan) -> str:
        # Will determine which muscle groups should be worked next based on their frequency and last day worked
        pass
