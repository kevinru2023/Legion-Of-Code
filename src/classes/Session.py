"""
C-05: Session
Auth: Nolan Cutler
Supports: EP-WOP-01, UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Workout[1]
"""

from models.Workout import Workout

class Session:
    def __init__(self):
        self._id: int = None
        self._day: str = ""
        self._notes: str = ""
        self._percieved_intensity: int = 0
        self._workout: Workout = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def day(self) -> str:
        return self._day

    @property
    def notes(self) -> str:
        return self._notes

    @property
    def percieved_intensity(self) -> int:
        return self._percieved_intensity

    @property
    def workout(self) -> Workout:
        return self._workout

    def store_notes(self, notes: str) -> None:
        self._notes = notes

    def track_id(self, id: int) -> None:
        self._id = id

    def log_workout_day(self, day: str) -> None:
        self._day = day

    def workout_intensity(self, intensity: int) -> None:
        self._percieved_intensity = intensity

    def log_workout(self, workout: Workout) -> None:
        self._workout = workout
