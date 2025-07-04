# File: goal_analyser.py
# Tool: GoalAnalyzerTool
"""
Yeh tool user ke health goal ko samajhta hai.
Jaise agar user likhe "lose 5kg in 2 months" — toh yeh usko structured format me convert karta hai.
"""

from openai_agents_sdk import Tool, tool
from pydantic import BaseModel
import re

# Output model for goal
class StructuredGoal(BaseModel):
    objective: str  # e.g., "lose"
    quantity: float  # e.g., 5
    unit: str  # e.g., "kg"
    duration: str  # e.g., "2 months"

@tool(name="GoalAnalyzerTool", description="User ke health goal ko structured format mein convert karta hai")
class GoalAnalyzerTool(Tool):

    async def run(self, input_text: str) -> StructuredGoal:
        # Basic regex for parsing goal
        match = re.search(r"(lose|gain)\s+(\d+\.?\d*)\s*(kg|lbs)\s+in\s+(\d+\s*(days|weeks|months))", input_text.lower())
        
        if not match:
            raise ValueError("Please provide a clear goal like 'lose 5kg in 2 months'.")

        objective, quantity, unit, duration, _ = match.groups()

        return StructuredGoal(
            objective=objective,
            quantity=float(quantity),
            unit=unit,
            duration=duration
        )
