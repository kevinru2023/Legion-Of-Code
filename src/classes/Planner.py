"""
C-04: Planner
Auth: Nolan Cutler
Supports EP-WOP-01, UR-APT-03, UR-APT-02, UR-APT-01, UR-BRBS
Collaborators: WorkoutPlan[0..*], Session [0..*]
"""

import json
from pathlib import Path

from .Session import Session
from .WorkoutPlan import WorkoutPlan


class Planner:
    def __init__(self, user=None):
        self._user = user
        self._plans = [] # workoutplans
        self._log = [] # sessions

        if self._user is not None and self._user.user_id:
            self.load_saved_plans()
            self.load_saved_log()

    def add_plan(self, plan: WorkoutPlan) -> None:
        self._plans.append(plan)
        self.save_plans()

    def list_plans(self) -> list[WorkoutPlan]:
        return self._plans

    def log_workout(self, session: Session) -> None:
        self._log.append(session)
        self.save_log()

    def edit_log(self, id: int, new_sess: Session) -> None:
        for index, session in enumerate(self._log):
            if session.id == id:
                self._log[index] = new_sess
                break

    def get_logs(self) -> list[Session]:
        return self._log

    def set_user(self, user) -> None:
        self._user = user
        if self._user is not None and self._user.user_id:
            self.load_saved_plans()
            self.load_saved_log()

    def get_user(self):
        return self._user

    def save_plans(self) -> str:
        # get workout-plan json for this user
        path = self._get_data_path("workout-plan")
        if path is None:
            return None

        data = []
        for plan in self._plans:
            data.append({
                "workout_plan": plan.workout_plan,
                "last_rest_day": plan.workout_plan,
                "current_streak": plan.workout_plan
            })

        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return str(path)

    def load_saved_plans(self) -> list[WorkoutPlan]:
        # get workout plan json for this user
        path = self._get_data_path("workout-plan")
        if path is None or not path.exists():
            self._plans = []
            return self._plans

        text = path.read_text(encoding="utf-8").strip()
        if not text:
            self._plans = []
            return self._plans

        # load plans from the workout-plan json
        self._plans = []
        for item in json.loads(text):
            plan = WorkoutPlan()
            plan._workout_plan = item.get("workout_plan", {})
            plan._last_rest_day = item.get("last_rest_day")
            plan._current_streak = item.get("current_streak", 0)
            self._plans.append(plan)

        return self._plans

    def save_log(self) -> str:
        path = self._get_data_path("workout-log")
        if path is None:
            return None

        data = []
        for session in self._log:
            data.append({
                "id": session.id,
                "day": session.day,
                "notes": session.notes,
                "percieved_intensity": session.percieved_intensity,
            })

        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return str(path)

    def load_saved_log(self) -> list[Session]:
        # log json (/src/prog-data/workout-log-{user id}.json)
        path = self._get_data_path("workout-log")
        if path is None or not path.exists():
            self._log = []
            return self._log

        text = path.read_text(encoding="utf-8").strip()
        if not text:
            self._log = []
            return self._log

        # 
        self._log = []
        for item in json.loads(text):
            session = Session()
            session._id = item.get("id")
            session._day = item.get("day", "")
            session._notes = item.get("notes", "")
            session._percieved_intensity = item.get("percieved_intensity", 0)
            self._log.append(session)

        return self._log

    def get_workout_plan_path(self) -> str:
        path = self._get_data_path("workout-plan")
        return str(path) if path else None

    def _get_data_path(self, prefix: str) -> Path:
        if self._user is None:
            return None

        user_id = self._user.user_id
        if not user_id:
            return None

        data_dir = Path(__file__).resolve().parent.parent / "prog-data"
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir / f"{prefix}-{user_id}.json"

