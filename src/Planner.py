"""
C-04: Planner
Auth: Nolan Cutler
Supports EP-WOP-01
Collaborators: Session, WorkoutPlan
"""
class Planner:
    # WorkoutPlan list
    plans = []
    # available workouts (stored as JSON)
    workouts = None    
    log = []
    
    def __init__(self, ...):
        # initialize class members/return singleton class

    def add_plan(self, plan: WorkoutPlan) -> None:
        # validate workout and store in WorkOut plans
        plan.validate() # or something similar

        Planner.plans.append(plan)

    def list_plans(self) -> list[WorkoutPlan]:
        return Planner.plans

    def log_workout(self, session: Session) -> None:
        Planner.log.append(session)

"""
C-05
Auth: Nolan Cutler
Supports EP-WOP-01
Collaborators: Workout
"""
@dataclass
class Session:
    day: str
    notes: str
    percieved_intensity: int
    workout: Workout



