"""
C-03: Workout
Auth: Nolan Cutler
Supports: EP-BRBS, UR-W0P-01
Collaborators: None
"""

@dataclass
class Workout:
    """
    Stores information specific to an exercise
    """

    self.name: str
    self.reps: int
    self.sets: int
    self.rest_time: int
    self.video_id: str
