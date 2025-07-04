
# File: meal_planner.py
# Tool: MealPlannerTool

"""
Yeh tool user ke diet type (vegetarian, keto, diabetic waghera) ke mutabiq
7 din ka meal plan banata hai.
"""

from openai_agents_sdk import Tool, tool
from pydantic import BaseModel
from typing import List

# Output model
class MealPlan(BaseModel):
    meals: List[str]  

@tool(name="MealPlannerTool", description="User ke dietary preference ke mutabiq 7 din ka meal plan banata hai")
class MealPlannerTool(Tool):

    async def run(self, diet_preference: str) -> MealPlan:
        base_meals = {
            "vegetarian": [
                "Day 1: Chickpea curry with rice",
                "Day 2: Veggie stir-fry with tofu",
                "Day 3: Lentil soup and whole wheat bread",
                "Day 4: Stuffed bell peppers",
                "Day 5: Palak paneer with brown rice",
                "Day 6: Grilled vegetable sandwich",
                "Day 7: Quinoa salad with beans"
            ],
            "keto": [
                "Day 1: Egg omelet with cheese",
                "Day 2: Chicken with broccoli",
                "Day 3: Zucchini noodles with pesto",
                "Day 4: Grilled salmon with spinach",
                "Day 5: Avocado chicken salad",
                "Day 6: Cauliflower crust pizza",
                "Day 7: Beef stir-fry with mushrooms"
            ],
            "default": [
                "Day 1: Mixed meal (rice, chicken, salad)",
                "Day 2: Pasta with veggies",
                "Day 3: Chicken soup and toast",
                "Day 4: Rice and lentils",
                "Day 5: Grilled fish and veggies",
                "Day 6: Tofu rice bowl",
                "Day 7: Egg sandwich and salad"
            ]
        }

        meals = base_meals.get(diet_preference.lower(), base_meals["default"])
        return MealPlan(meals=meals)
