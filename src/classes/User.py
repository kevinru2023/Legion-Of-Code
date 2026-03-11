"""
C-07: User
Auth: Niki Pandya
Supports: UR-WP-01, UR-WP-02, UR-WP-03, UR-APT-01, UR-WOP-01
Collaborators: Planner[1]
"""

import json
from pathlib import Path

from classes.Planner import Planner
from classes.Session import Session

class User:
    """
    Represents a user of the workout tracking application.
    A User owns workout plans and workout session history.
    """

    def __init__(self, user_name: str, planner: Planner):
        self._planner: Planner = planner
        self._user_name: str = user_name
        with open(Path(__file__).parent / "../data/users.json", "r") as f:
            data = json.load(f)
            if(user_name in data):
                self._name: str = data[user_name]["name"]
                self._email: str = data[user_name]["email"]
                return
        self._name: str = input("Enter your name: ")
        self._email: str = input("Enter your email: ")
        self.update_profile(self._name, self._email)

    # ------------------------
    # Session Management
    # ------------------------

    def add_session(self, session: Session) -> None:
        self._planner.log_workout(session)

    def get_sessions(self) -> list[Session]:
        return self._planner.get_logs()

    # ------------------------
    # Profile Management
    # ------------------------

    def update_profile(self, name: str, email: str) -> None:
        self._name = name
        self._email = email
        with open(Path(__file__).parent / "../data/users.json", "r+") as f:
            data = json.load(f)
            data[self._user_name] = {"name": self._name, "email": self._email}
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()


    def get_user_info(self) -> dict:
        return {"user_name": self._user_name, "name": self._name, "email": self._email}

    def get_planner(self) -> Planner:
        return self._planner