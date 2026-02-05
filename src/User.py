"""
C-07: User
Auth: Niki Pandya
Supports: UR-WP-01, UR-WP-02, UR-WP-03, UR-APT-01, UR-WOP-01
Collaborators: Planner[1]
"""

from Planner import Planner
from WorkoutPlan import WorkoutPlan
from Session import Session

class User:
    def __init__(self, user_id: str, name: str, email: str):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._planner = Planner()
        
    def add_workout_plan(self, plan: WorkoutPlan) -> None:
        self._planner.add_plan(plan)

    def remove_workout_plan(self, plan_id: int) -> bool:
        return self._planner.remove_plan(plan_id)

    def get_plans(self) -> list[WorkoutPlan]:
        return self._planner.list_plans()

    def add_session(self, session: Session) -> None:
        self._planner.log_workout(session)

    def get_sessions(self) -> list[Session]:
        return self._planner.get_logs()

    def get_planner(self) -> Planner:
        return self._planner
