"""
C-05: Session
Auth: Nolan Cutler
Supports: EP-WOP-01, UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Workout[1]
"""
from datetime import date as date_type

class Session:
    def __init__(self):
        self._id = None
        self._day = ""
        self._date = None # Added -> Date using datetime import
        self._duration_minutes = 0 # Added -> Time spent in workout
        self._notes = ""
        self._perceived_intensity = 0
        self._workout = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def day(self) -> str:
        return self._day
    
    @property # Added
    def date(self) -> date_type:
        return self._date
    
    @property # Added
    def duration_minutes(self) -> int:
        return self._duration_minutes
    
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
        self._notes = notes

    def track_id(self, id: int) -> None:
        self._id = id

    def log_workout_day(self, day: str) -> None:
        self._day = day
        
    def log_workout_date(self, date: date_type) -> None: # Added
        self._date = date
    
    def log_duration(self, minutes: int) -> None: # Added
        self._duration_minutes = minutes

    def workout_intensity(self, intensity: int) -> None:
        self._perceived_intensity = intensity

    def log_workout(self, workout) -> None:
        self._workout = workout
