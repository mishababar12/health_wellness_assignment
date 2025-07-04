
# File: agent.py
# Agent: HealthWellnessPlannerAgent

"""
Yeh main agent hai jo sab tools aur agents ko handle karega.
User kuch bhi likhe, yeh decide karta hai ke konsa tool ya agent use hoga.

Use hone wale tools:
- GoalAnalyzerTool
- MealPlannerTool
- WorkoutRecommenderTool
- CheckinSchedulerTool
- ProgressTrackerTool

Handoff hone wale agents:
- InjurySupportAgent
- NutritionExpertAgent
- EscalationAgent

"""

from openai_agents_sdk import Agent, agent
from typing import Union

from context import UserSessionContext
from tools.goal_analyser import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheckinSchedulerTool
from tools.tracker import ProgressTrackerTool

from agents.injury_support_agent import InjurySupportAgent
from agents.nutrition_expert_agent import NutritionExpertAgent
from agents.escalation_agent import EscalationAgent

from guardrails import validate_goal_input, validate_diet_input

@agent(name="HealthWellnessPlannerAgent", description="User ke health goals ke liye personalized plan banata hai")
class HealthWellnessPlannerAgent(Agent):
    tools = [
        GoalAnalyzerTool(),
        MealPlannerTool(),
        WorkoutRecommenderTool(),
        CheckinSchedulerTool(),
        ProgressTrackerTool()
    ]

    handoffs = [
        InjurySupportAgent(),
        NutritionExpertAgent(),
        EscalationAgent()
    ]

    async def run(self, input_text: str, context: UserSessionContext) -> Union[str, dict]:
        lowered = input_text.lower()

        # 🩺 Handoff: Injury-related
        if any(kw in lowered for kw in ["knee pain", "leg pain", "back pain", "injury", "hurt", "pain"]):
            context.handoff_logs.append("InjurySupportAgent triggered")
            return await InjurySupportAgent().run(input_text)

        # 🍱 Handoff: Complex dietary needs
        if any(kw in lowered for kw in ["diabetes", "diabetic", "allergy", "gluten", "blood sugar"]):
            context.handoff_logs.append("NutritionExpertAgent triggered")
            return await NutritionExpertAgent().run(input_text)

        # 🧑‍🏫 Handoff: Human trainer
        if any(kw in lowered for kw in ["real trainer", "talk to coach", "human trainer", "personal coach"]):
            context.handoff_logs.append("EscalationAgent triggered")
            return await EscalationAgent().run(input_text)

        # 🎯 Goal: Weight goals
        if "lose" in lowered or "gain" in lowered or "reduce" in lowered:
            if not validate_goal_input(input_text):
                return "⚠️ Please provide a valid goal like 'lose 5kg in 2 months'."
            result = await GoalAnalyzerTool().run(input_text)
            context.goal = result.dict()
            return f"🎯 Goal set: {result.objective} {result.quantity} {result.unit} in {result.duration}."

        # 🥗 Diet preference
        if any(diet in lowered for diet in ["vegetarian", "keto", "diabetic", "vegan"]):
            diet_type = lowered.strip()
            if not validate_diet_input(diet_type):
                return "⚠️ Please provide a valid diet type (vegetarian, keto, diabetic, vegan)."
            context.diet_preferences = diet_type
            result = await MealPlannerTool().run(diet_type)
            context.meal_plan = result.meals
            return "\n".join(result.meals)


        # 🏋️‍♀️ Workout recommendation
        levels = ["beginner", "intermediate", "advanced"]
        for level in levels:
            if level in lowered:
                result = await WorkoutRecommenderTool().run(level)
                context.workout_plan = result.workouts
                return "\n".join(f"{w['day']}: {w['workout']}" for w in result.workouts)


        # 🕓 Schedule check-ins
        if "schedule" in lowered or "start from" in lowered or any(char.isdigit() for char in input_text):
            import re
            match = re.search(r"\d{4}-\d{2}-\d{2}", input_text)
            if match:
                date = match.group()
                result = await CheckinSchedulerTool().run(date)
                return f"✅ Check-ins scheduled starting from {date}.\n{result}"

        # ✅ Progress update
        if "completed" in lowered or "finished workout" in lowered:
            result = await ProgressTrackerTool().run(input_text, context)
            return f"✅ Progress updated: {result}"

        # 📩 Fallback message
        return (
            "💡 I'm here to help! You can say things like:\n"
            "- 'I want to lose 5kg in 2 months'\n"
            "- 'I'm vegetarian'\n"
            "- 'I'm diabetic'\n"
            "- 'I have knee pain'\n"
            "- 'I'm a beginner'\n"
            "- 'I'm intermediate'\n"
            "- 'I'm advanced'\n"
            "- 'I completed my 3rd workout'\n"
            "- 'Schedule from 2025-07-01'\n"
            "- 'I want to talk to a real trainer'"
        )
