"""
C-08: ProgressAnalyzer
Auth: Alex Cortes
Supports: UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Session [...], Planner[...], User[...]
"""

from classes.Planner import Planner
from classes.Session import Session
from classes.WorkoutPlan import WorkoutPlan
from classes.User import User

from datetime import date, timedelta
from collections import defaultdict
from typing import Optional


class ProgressAnalyzer:
    """
    Primary Purpose: Manages the calculation of statistics and tracking of progress.
    """

    def __init__(
        self,
        sessions: Optional[list[Session]] = None,
        date_range: Optional[tuple[date, date]] = None,
        user: Optional[User] = None,
        planner: Optional[Planner] = None,
    ):
        if user:
            self.sessions: list[Session] = user.get_sessions()
        elif planner:
            self.sessions: list[Session] = planner.get_logs()
        else:
            self.sessions: list[Session] = sessions or []
        self.date_range: tuple[date, date] = date_range or ()

    def calculate_stats(self) -> dict[str, int | float]:
        total: int = len(self.sessions)

        if not self.sessions:
            return {"total_workouts": 0, "avg_per_week": 0, "current_streak": 0}

        weeks: set[tuple[int, int]] = set()
        for s in self.sessions:
            try:
                d: date = date.fromisoformat(s.day)
                weeks.add(d.isocalendar()[:2])  # (year, week number)
            except (ValueError, TypeError):
                pass

        avg_per_week: float = round(total / len(weeks), 2) if weeks else 0

        logged_days: set[date] = set()
        for s in self.sessions:
            try:
                logged_days.add(date.fromisoformat(s.day))
            except (ValueError, TypeError):
                pass

        streak: int = 0
        check: date = date.today()
        while check in logged_days:
            streak += 1
            check -= timedelta(days=1)

        return {"total_workouts": total, "avg_per_week": avg_per_week, "current_streak": streak}

    def weekly_stats(self, weeks: int = 4) -> list[dict[str, int | str]]:
        weekly_data: list[dict[str, int | str]] = []

        buckets: defaultdict[tuple[int, int], int] = defaultdict(int)
        for s in self.sessions:
            try:
                d: date = date.fromisoformat(s.day)
                buckets[d.isocalendar()[:2]] += 1
            except (ValueError, TypeError):
                pass

        today: date = date.today()
        for i in range(weeks):
            week_start: date = today - timedelta(weeks=i)
            key: tuple[int, int] = week_start.isocalendar()[:2]
            weekly_data.append(
                {
                    "week": f"Week -{i} ({week_start.strftime('%b %d')})",
                    "workout_count": buckets.get(key, 0),
                }
            )

        return list(reversed(weekly_data))

    def improvement_insights(self) -> list[str]:
        insights: list[str] = []

        if len(self.sessions) < 3:
            insights.append("Log more workouts for better analysis.")
            return insights

        stats: dict[str, int | float] = self.calculate_stats()
        if stats["avg_per_week"] < 3:
            insights.append("Try to hit at least 3 workouts per week for consistent progress.")
        if stats["current_streak"] == 0:
            insights.append("No active streak — get back at it today!")
        elif stats["current_streak"] >= 7:
            insights.append(f"Great job! You're on a {stats['current_streak']}-day streak!")

        return insights

    def generate_report(self) -> dict[str, dict | list]:
        """Generate comprehensive progress report"""
        return {
            "basic_stats": self.calculate_stats(),
            "weekly_stats": self.weekly_stats(),
            "improvement_areas": self.improvement_insights(),
        }