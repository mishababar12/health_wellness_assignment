
# File: nutrition_expert_agent.py
# Agent: NutritionExpertAgent

"""
Yeh agent un logon ke liye hai jinko health condition hai (jaise diabetes, allergy).
Yeh dietary advice deta hai, safe foods recommend karta hai.
"""

from openai_agents_sdk import Agent, agent
from pydantic import BaseModel

class NutritionAdvice(BaseModel):
    message: str

@agent(name="NutritionExpertAgent", description="Complex dietary conditions jaise diabetes, allergies ke liye help deta hai")
class NutritionExpertAgent(Agent):

    async def run(self, input_text: str) -> NutritionAdvice:
        return NutritionAdvice(
            message="Based on your input, we suggest consulting a dietitian. Meanwhile, avoid high sugar/carbs and prefer high-fiber, low-GI foods."
        )
