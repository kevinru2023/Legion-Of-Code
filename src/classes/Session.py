"""
C-05: Session
Auth: Nolan Cutler
Supports: EP-WOP-01, UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Workout[1]
"""


class Session:
    def __init__(self):
        self._id = None
        self._day = ""
        self._notes = ""
        self._percieved_intensity = 0
        self._workout = None

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
    def workout(self):
        return self._workout

    def store_notes(self, notes: str) -> None:
        pass

    def track_id(self, id: int) -> None:
        return None

    def log_workout_day(self, day: str) -> None:
        return None

    def workout_intensity(self, intensity: int) -> None:
        return None

    def log_workout(self, workout) -> None:
        return None
