"""
C-06: Viewer
Auth: Nolan Cutler
Supports EP-WOP-01, UR-IID-01, UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Planner[1] 
"""
class Viewer:
    """
    This will probably exist in the frontend in some ohter language/framework; this 
    "code" is just a tentative outline for the structure of how that class will be implemented.
    """
    def __init__(self):
        # set config (darkmode, layout, etc)...

        self._planner = Planner()
        
    def create_plan(self) -> None:
        # display workout plan editor and construct WorkoutPlan obj
        plan = _create_gui()

        # pass plan to Planner
        self._planner.add_plan(plan)

    def view_plans(self) -> None:
        # load all plans
        plans = self._planner.list_plans()

        # display all plans in GUI
        _view_gui(plans)

    def log_workout(self) -> None:
        # display GUI for user to log workout and construct session object
        session = _log_workout_gui()

        # log workout to planner
        self._planner.log_workout(session)

    def view_logs(self) -> None:
        # pullup log viewer/editor
        _logs_gui()

    def select_workout_plan(self) -> WorkoutPlan:
        # load all plans
        plans = self._planner.list_plans()
        
        # display all plans for selection
        return _select_gui(plans)

    def _view_workout_session(session: Session) -> None:
        # display session info

    def _logs_gui(self) -> None:
        # display gui for viewing/editing logs

    # note: this will entail viewing videos, which will likely
    # need to be stored remotely
    def _select_plan_gui(self) -> None:
        # let user select plan 

    # note: this will entail viewing videos, which will likely
    # need to be stored remotely
    def _view_plans_gui(self) -> None:
        # display plans for viewing

    def _log_workout_gui(self) -> Session:
        # display gui for constructing workout session

    def _create_plan_gui(self) -> WorkoutPlan:
        # display gui for creating a WorkoutPlan

