"""
C-08: ProgressAnalyzer
Auth: Alex Cortes
Supports: UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Session [...], Planner[...], User[...]
"""

from Planner import Session, Planner
from Workout import Workout, WorkoutPlan
from User import User


class ProgressAnalyzer:
    """
    Primary Purpose: Manages the calculation of statistics and tracking of progress.
    """

    def __init__(self, sessions=None, date_range=None, user=None, planner=None):
        if user:
            self.sessions = user.get_sessions()
        elif planner:
            self.sessions = planner.get_logs()
        else:
            self.sessions = sessions  # list of Session objects
        self.stats = {}
        self.date_range = ()  # Tuple (start_date, end_date)

    # Basic statistics
    def calculate_stats(self):
        total = len(self.sessions)
        if not self.sessions:
            avg_per_week = 0
            streak = 0

        return {"total_workouts": total, "avg_per_week": avg_per_week, "current_streak": streak}

    def weekly_stats(self, weeks=4):
        weekly_data = []
        for i in range(weeks):
            weekly_data.append(
                {
                    "week": f"Week {i+1}",
                    "workout_count": 0,
                    "total_duration": 0,
                }
            )
        return weekly_data

    # Progress tracking
    def improvement_insights(self):
        insights = []
        if len(self.sessions) < 3:
            insights.append("Log more workouts for better analysis")

        # TODO: add default insights for higher amounts of sessions.

        return insights

    def generate_report(self):
        """
        Generate comprehensive progress report
        """
        return {
            "basic_stats": self.calculate_stats(),
            "weekly_stats": self.weekly_stats(),
            "improvement_areas": self.improvement_insights(),
        }
