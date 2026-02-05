"""
C-04: Planner
Auth: Nolan Cutler
Supports EP-WOP-01, UR-APT-03, UR-APT-02, UR-APT-01, UR-BRBS
Collaborators: WorkoutPlan[0..*], Session [0..*] 
"""
class Planner:
    _workouts = None
    def __init__(self, ...):
        # WorkoutPlan list
        _plans = []
         # available workouts (stored as JSON)
        _log = []

    def add_plan(self, plan: WorkoutPlan) -> None:
        # validate workout and store in WorkOut plans
        plan.validate() # or something similar

        self._plans.append(plan)

    def list_plans(self) -> list[WorkoutPlan]:
        return self._plans

    def log_workout(self, session: Session) -> None:
        self._log.append(session)

    def edit_log(self, id: int, new_sess: Session) -> None:
        # edit existing log entry with id == id parameter

    def get_logs(self) -> list[Session]:
        return self._log

"""
C-05
Auth: Nolan Cutler
Supports EP-WOP-01, UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Workout[1]
"""
@dataclass
class Session:
    id: int
    day: str
    notes: str
    percieved_intensity: int
    workout: Workout



