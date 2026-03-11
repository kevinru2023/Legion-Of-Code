"""
C-04: Planner
Auth: Nolan Cutler
Supports EP-WOP-01, UR-APT-03, UR-APT-02, UR-APT-01, UR-BRBS
Collaborators: WorkoutPlan[0..*], Session [0..*]
"""

from classes.WorkoutPlan import WorkoutPlan
from classes.Session import Session
from models.Workout import Workout

class Planner:
    def __init__(self):
        self._plans: list[WorkoutPlan] = []
        self._logs: list[Session] = []
        self._workouts: list[Workout] = []

    def add_plan(self, plan: WorkoutPlan) -> None:
        self._plans.append(plan)

    def remove_plan(self, id: int) -> None:
        for i, plan in enumerate(self._plans):
            if plan.id == id:
                del self._plans[i]
                return

    def list_plans(self) -> list[WorkoutPlan]:
        return self._plans

    def log_workout(self, session: Session) -> None:
        self._logs.append(session)

    def edit_log(self, id: int, new_sess: Session) -> None:
        for i, sess in enumerate(self._logs):
            if sess.id == id:
                self._logs[i] = new_sess
                return

    def get_logs(self) -> list[Session]:
        return self._logs
