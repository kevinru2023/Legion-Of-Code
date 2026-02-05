"""
C-07: User
Auth: Niki Pandya
Supports: UR-WP-01, UR-WP-02, UR-WP-03, UR-APT-01, UR-WOP-01
Collaborators: Planner[1]
"""

class User:
    def __init__(self, user_id, name, email):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._planner = Planner()

    def add_workout_plan(self):
        self._planner.add_plan(plan)

    def remove_workout_plan(self, plan_id):
        for plan in self._planner.list_plans():
            if plan.id == plan_id:
                self._planner.remove(plan)
                return True
        return False

    def add_session(self, session):
        self.log_workout(session)

    def get_plans(self):
        return self._planner.list_plans()

    def get_sessions(self):
        return self.get_logs()
