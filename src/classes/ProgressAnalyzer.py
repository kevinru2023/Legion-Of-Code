"""
C-08: ProgressAnalyzer
Auth: Alex Cortes
Supports: UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Session [...], Planner[...], User[...]
"""


from .WorkoutPlan import WorkoutPlan
from .User import User
from datetime import date as date_type, timedelta


class ProgressAnalyzer:
    """
    Primary Purpose: Manages the calculation of statistics and tracking of progress.
    
    READ THESE NOTES:
        This class assumes that it will be given a list of Sessions. 
        Tracing where this list of session comes from:
            [Planner.py] get_logs(self) -> list[Session] --
                [User.py] get_sessions(self) -> list[Session] --
                     -> [ProgressAnalyzer.py] 
                        __init__(self, user, session): 
                            if user:
                                self.sessions = user.get_sessions()
                            else:
                                self.sessions = sessions or []  # list of Session objects
                                
        TLDR; Sessions can be supplied directly or retrived from User object
              Session.py has _date and _duration_minutes attributes added for this class.
              
              If the session logs (list of kept sessions) is EVER read from JSON,
                    it breaks all statistics calculations. 
    """
    # user -> Retrieves the user's completed session (if exists)
    # session -> List of COMPLETED sessions
    def __init__(self, user=None, sessions=None):
        if user:
            self.sessions = user.get_sessions()
        else:
            self.sessions = sessions or []  # list of Session objects
    
    def calculate_stats(self):
        """
        Aggregate single‑week statistics over the loaded sessions.

        Returns:
            dict: Summary metrics focused on the current set of logs, including:
                  - total_workouts
                  - total_minutes
                  - avg_minutes
                  - avg_rpe
                  - current_streak
                  - most_common_day
                  - hardest_workout
        """
        total_sessions = len(self.sessions)
        if not self.sessions:  # No sessions
            return {
                "total_workouts": 0,
                "total_minutes": 0,
                "avg_minutes": 0,
                "avg_rpe": 0,
                "current_streak": 0,
                "most_common_day": None,
                "hardest_workout": None,
            }

        # Durations and intensity
        durations = [
            getattr(s, "duration_minutes", 0) for s in self.sessions
            if getattr(s, "duration_minutes", 0) > 0
        ]
        total_minutes = sum(durations) if durations else 0
        avg_minutes = round(total_minutes / len(durations), 1) if durations else 0

        rpes = [getattr(s, "perceived_intensity", 0) for s in self.sessions]
        avg_rpe = round(sum(rpes) / len(rpes), 1) if rpes else 0

        # Current streak still uses calendar dates if available
        # current_streak = self.calculate_streak()

        # Most common workout day across the logs
        day_counts: dict[str, int] = {}
        for s in self.sessions:
            day = getattr(s, "day", None)
            if day:
                day_counts[day] = day_counts.get(day, 0) + 1
        most_common_day = max(day_counts, key=day_counts.get) if day_counts else None

        # Hardest workout (highest perceived intensity)
        hardest_session = max(self.sessions, key=lambda s: getattr(s, "perceived_intensity", 0))
        w = getattr(hardest_session, "workout", None)
        hardest_workout_name = getattr(w, "name", None) if w else None

        return {
            "total_workouts": total_sessions,
            "total_minutes": total_minutes,
            "avg_minutes": avg_minutes,
            "avg_rpe": avg_rpe,
            # "current_streak": current_streak,
            "most_common_day": most_common_day,
            "hardest_workout": hardest_workout_name,
        }

    # Insight text
    def improvement_insights(self):
        """
        Generates motivational insight messages based on streak and workout duration.

        Returns:
            list: A list of insight strings to display to the user.
        """
        
        insights = [] 
        if len(self.sessions) < 3:
            insights.append("Log more workouts for insights.")
            return insights # Exit for no crash :)
        # Duration
        durations = [s.duration_minutes for s in self.sessions]
        # Guard against sessions reconstructed from JSON that may not yet
        # have a duration attached.
        durations = [
            getattr(s, "duration_minutes", 0) for s in self.sessions
            if getattr(s, "duration_minutes", 0) > 0
        ]
        if not durations:
            return insights

        avg_duration = sum(durations) / len(durations)

        if avg_duration < 20:
            insights.append("Even short sessions count — try pushing to 20 minutes next time!")
        elif avg_duration < 45:
            insights.append(f"You're averaging {round(avg_duration)} minutes per workout — nice work!")
        else:
            insights.append(f"Averaging {round(avg_duration)} minutes per session — outstanding effort!")
        return insights
    
    # Generates all statistics (general + weekly) and motivational improvement insights
    def generate_report(self):
        """
        Generate comprehensive progress report statistics
        """
        return {
            "basic_stats": self.calculate_stats(),
            "improvement_areas": self.improvement_insights(),
        }

    def statistics(user):
        """
        Convenience helper used by the GUI (Viewer.view_statistics).

        Builds a readable multi‑line string so it can be dropped directly into
        a Tkinter label while still being friendly to console output if needed.
        """
        try:
            user_stats = ProgressAnalyzer(user)
            report = user_stats.generate_report()
            basic_stats = report.get("basic_stats", {}) or {}
            insights = report.get("improvement_areas", []) or []
        except Exception as exc:
            # Fallback so the GUI never crashes if something unexpected happens.
            return f"Unable to compute statistics:\n{exc}"

        lines: list[str] = []
        lines.append("=== Workout Statistics ===")
        total_workouts = basic_stats.get("total_workouts", 0)
        total_minutes = basic_stats.get("total_minutes", 0)
        avg_minutes = basic_stats.get("avg_minutes", 0)
        avg_rpe = basic_stats.get("avg_rpe", 0)
        most_common_day = basic_stats.get("most_common_day") or None
        hardest_workout = basic_stats.get("hardest_workout") or None

        lines.append(f"Total Workouts: {total_workouts}")
        lines.append(f"Total Minutes: {total_minutes}")
        lines.append(f"Average Minutes per Session: {avg_minutes}")
        lines.append(f"Average RPE: {avg_rpe}")
        if most_common_day:
            lines.append(f"Most Common Training Day: {most_common_day}")
        if hardest_workout:
            lines.append(f"Hardest Workout: {hardest_workout}")
        lines.append("")  # spacer

        if insights:
            lines.append("Workout Insights:")
            for item in insights:
                lines.append(f"  • {item}")

        return "\n".join(lines)
