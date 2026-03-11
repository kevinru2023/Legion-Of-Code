"""
C-05: Session
Auth: Nolan Cutler
Supports: EP-WOP-01, UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Workout[1]
"""

import json
from pathlib import Path

from models.Workout import Workout

class Session:
    def __init__(self, id: int, day: str, notes: str, percieved_intensity: int):
        self._id: int = id
        self._day: str = day
        self._notes: str = notes
        self._percieved_intensity: int = percieved_intensity
        self._workout = Workout(self)

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

    def load_data(self):
        file = Path(f"session_{self._id}.json")
        if file.exists():
            with open(file, "r") as f:
                return json.load(f)
        return {}

    def save_data(self, data):
        with open(f"session_{self._id}.json", "w") as f:
            json.dump(data, f, indent=4)

    def track_id(self, id: int) -> None:
        data = self.load_data()
        data["Session ID"] = id
        self.save_data(data)

    def store_notes(self, notes: str) -> None:
        data = self.load_data()
        data["Notes"] = notes
        self.save_data(data)

    def log_workout_day(self, day: str) -> None:
        data = self.load_data()
        data["Date"] = day
        self.save_data(data)

    def workout_intensity(self, intensity: int) -> None:
        data = self.load_data()
        data["Intensity"] = intensity
        self.save_data(data)

    def log_workout(self, workout) -> None:
        data = self.load_data()
        data["Workout"] = workout
        self.save_data(data)
