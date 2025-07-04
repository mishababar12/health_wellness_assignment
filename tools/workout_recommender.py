
# File: workout_recommender.py
# Tool: WorkoutRecommenderTool
"""
Yeh tool user ke fitness level (beginner, intermediate, advanced) ke mutabiq
ek hafte ka workout plan return karta hai.
"""

from openai_agents_sdk import Tool, tool
from pydantic import BaseModel
from typing import List, Dict

# Output model
class WorkoutPlan(BaseModel):
    workouts: List[Dict[str, str]]  # Har din ka ek structured workout

@tool(name="WorkoutRecommenderTool", description="User ke fitness level ke mutabiq weekly workout plan deta hai")
class WorkoutRecommenderTool(Tool):

    async def run(self, experience_level: str) -> WorkoutPlan:
        plans = {
            "beginner": [
                {"day": "Day 1", "workout": "30 min walk + light stretching"},
                {"day": "Day 2", "workout": "15 min bodyweight exercises"},
                {"day": "Day 3", "workout": "Rest or yoga"},
                {"day": "Day 4", "workout": "20 min cardio (jumping jacks, march in place)"},
                {"day": "Day 5", "workout": "Core workout (planks, crunches)"},
                {"day": "Day 6", "workout": "Light full-body workout"},
                {"day": "Day 7", "workout": "Rest or walk"}
            ],
            "intermediate": [
                {"day": "Day 1", "workout": "45 min cardio + strength mix"},
                {"day": "Day 2", "workout": "Upper body strength"},
                {"day": "Day 3", "workout": "HIIT workout"},
                {"day": "Day 4", "workout": "Lower body strength"},
                {"day": "Day 5", "workout": "Core + cardio"},
                {"day": "Day 6", "workout": "Yoga or flexibility"},
                {"day": "Day 7", "workout": "Rest"}
            ],
            "advanced": [
                {"day": "Day 1", "workout": "60 min strength training"},
                {"day": "Day 2", "workout": "HIIT + weight training"},
                {"day": "Day 3", "workout": "Endurance cardio (running or cycling)"},
                {"day": "Day 4", "workout": "Plyometrics + mobility"},
                {"day": "Day 5", "workout": "Upper/lower split strength"},
                {"day": "Day 6", "workout": "Active recovery or yoga"},
                {"day": "Day 7", "workout": "Rest"}
            ]
        }

        selected_plan = plans.get(experience_level.lower(), plans["beginner"])
        return WorkoutPlan(workouts=selected_plan)
