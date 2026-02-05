"""
C-07: User
Auth: Niki Pandya
Supports: UR-WP-01, UR-WP-02, UR-WP-03, UR-APT-01, UR-WOP-01
Collaborators: WorkoutPlan, Session
"""

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.workout_plans = []
        self.workout_sessions = []

    def add_workout_plan(self, plan):
        self.workout_plans.append(plan)

    def remove_workout_plan(self, plan_id):
        for plan in self.workout_plans:
            if getattr(plan, "plan_id", None) == plan_id:
                self.workout_plans.remove(plan)
                return True
        return False

    def add_session(self, session):
        self.workout_sessions.append(session)

    def get_plans(self):
        return self.workout_plans

    def get_sessions(self):
        return self.workout_sessions
