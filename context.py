
# File: context.py
# Purpose: User ka session data store karna (jaise ke ek memory)

"""
Yeh file ek class define karti hai: UserSessionContext
Jo user ke saath related data ko store karta hai, jaise:

name: user ka naam
uid: user ka ID
goal: user ka health goal (jaise 'lose 5kg in 2 months')
diet_preferences: user ki diet choice (jaise vegetarian)
workout_plan: weekly workout data
meal_plan: 7 din ka khanay ka plan
injury_notes: agar koi chot ya restriction ho
handoff_logs: kis agent ke paas user ko bheja gaya
completed_workouts: user ne kitne workouts complete kiye
progress_logs: user ka progress record (daily ya weekly)

Yeh context sab agents aur tools ko diya jata hai takay user ka pichla data yaad rakha ja sake.

"""

from typing import Optional, List, Dict
from pydantic import BaseModel

class UserSessionContext(BaseModel):
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    completed_workouts: int = 0
    progress_logs: List[Dict[str, str]] = []
