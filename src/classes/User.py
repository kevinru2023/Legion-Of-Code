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
    """
    Represents a user of the workout tracking application.
    A User owns workout plans and workout session history.
    """

    def __init__(self, user_id: str, name: str, email: str):
        self._user_id: str = user_id
        self._name: str = name
        self._email: str = email
        self._planner: Planner = Planner()

    # ------------------------
    # Workout Plan Management
    # ------------------------

    def add_workout_plan(self, plan: WorkoutPlan) -> None:
        """Adds a workout plan to the user's planner."""
        self._planner.add_plan(plan)

    def get_plans(self) -> list[WorkoutPlan]:
        """Returns all workout plans owned by the user."""
        return self._planner.list_plans()

    # ------------------------
    # Session Management
    # ------------------------

    def add_session(self, session: Session) -> None:
        """Logs a completed workout session."""
        self._planner.log_workout(session)

    def get_sessions(self) -> list[Session]:
        """Returns all logged workout sessions."""
        return self._planner.get_logs()

    # ------------------------
    # Profile Management
    # ------------------------

    def update_profile(self, name: str, email: str) -> None:
        """Updates the user's profile information."""
        self._name = name
        self._email = email

    def get_user_info(self) -> dict:
        """Returns basic user information."""
        return {"user_id": self._user_id, "name": self._name, "email": self._email}

    # ------------------------
    # Planner Access
    # ------------------------

    def get_planner(self) -> Planner:
        """Returns the associated planner."""
        return self._planner
