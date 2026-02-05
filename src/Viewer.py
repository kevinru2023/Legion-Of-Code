"""
Auth: Nolan Cutler
Supports EP-WOP-01
Collaborators: Session, Planner, WorkoutPlan
"""
class Viewer:
    """
    This will probably exist in the frontend in some ohter language/framework; this 
    "code" is just a tentative outline for the structure of how that class will be implemented.
    """
    def __init__(self, ...):
        # set config (darkmode, layout, etc)...

        self.planner = Planner()
        
    def create_plan(self) -> None:
        # display workout plan editor and construct WorkoutPlan obj
        plan = _create_gui()

        # pass plan to Planner
        self.planner.add_plan(plan)

    def view_plans(self) -> None:
        # load all plans
        plans = self.planner.list_plans()

        # display all plans in GUI
        _view_gui(plans)

    def log_workout(self) -> None:
        # display GUI for user to log workout and construct session object
        session = _log_workout_gui()

        # log workout to planner
        self.planner.log_workout(session)

    def select_workout_plan(self) -> WorkoutPlan:
        # load all plans
        plans = self.planner.list_plans()
        
        # display all plans for selection
        return _select_gui(plans)

    # note: this will entail viewing videos, which will likely
    # need to be stored remotely
    def _select_gui(self, plans: list[WorkoutPlan]) -> None:
        # display plans for selection

    # note: this will entail viewing videos, which will likely
    # need to be stored remotely
    def _view_gui(self, plans: list[WorkoutPlan]) -> None:
        # display plans for viewing

    def _log_workout_gui(self) -> Session:
        # display gui for constructing workout session

    def _create_gui(self) -> WorkoutPlan:
        # display gui for creating a WorkoutPlan

