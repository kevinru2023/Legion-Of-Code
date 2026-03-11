"""
C-08: ProgressAnalyzer
Auth: Alex Cortes
Supports: UR-APT-03, UR-APT-02, UR-APT-01
Collaborators: Session [...], Planner[...], User[...]
"""

from Planner import Planner
from WorkoutPlan import WorkoutPlan
from User import User
from datetime import date as date_type
"""
    What a json entry would look like:
    
    "mon": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                "name": { "type": "string" },
                "reps": { "type": "integer" },
                "sets": { "type": "integer" },
                "rest_time": { "type": "integer" },
                "video_id": { "type": "string" }
                },
                "required": ["name", "reps", "sets", "rest_time", "video_id"],
                "additionalProperties": false
            }
            },
"""


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

    # Calculate [completed] User Workout Statistics 
    # TODO: Intended statistics:
    #       Total Workouts -- Integer
    #       Streaks -- Integer
    #       Average Workouts (that week) -- time
    def calculate_stats(self):
        total_sessions = len(self.sessions)
        if not self.sessions: # No sessions
            return {
            "total_workouts": 0,
            "avg_per_week": 0,
            "current_streak": 0
            }     
            
        # Average Per Week 
        # Basic general average -> # of workouts total / number of weeks spanned
        # Getting the weeks spanned requires:
        #   # of days from (current date - earliest date) of ALL sessions / 7 (week length)
        #       DONT DIVIDE BY ZERO AT ALL COSTS
        #       This can happen IF there is only one week's worth of workouts logged
        dates = sorted([s.date for s in self.sessions]) 
        num_weeks = max(((dates[-1] - dates[0]).days / 7), 1) # without max(,1), zero is possible
        avg_per_week = round(total_sessions / num_weeks, 1)
        
        # Streaks (basic implementation)
        distinct_days = sorted({s.date for s in self.sessions})
        current_streak = 0
        for i in range(1, len(distinct_days)):
            # Count forwards, and if the dates are exactly 1 day apart, streak++
            if (distinct_days[i] - distinct_days[i-1]).days == 1:
                current_streak += 1
            else:
                current_streak = 1
        
        return {
            "total_workouts": total_sessions,
            "avg_per_week": avg_per_week,
            "current_streak": current_streak}
        

    def weekly_stats(self, weeks=4):
        today = date_type.today()
        weekly_data = []
        for i in range(weeks):
            # Each iteration is week #
            
            
            
            # Duration
            # Workouts total that week
            
            weekly_data.append(
                {
                    "week": f"Week #{i+1}",
                    "workout_count": count,
                    "total_duration": duration,
                }
            )
    
        return weekly_data

    # Insight text
    def improvement_insights(self):
        insights = [] 
        if len(self.sessions) < 3:
            insights.append("Log more workouts for an analysis :)")

        # TODO: add default insights for higher amounts of sessions.
        # if 
        # return insights

    def generate_report(self):
        """
        Generate comprehensive progress report
        """
        return {
            "basic_stats": self.calculate_stats(),
            "weekly_stats": self.weekly_stats(),
            "improvement_areas": self.improvement_insights(),
        }
