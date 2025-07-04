
# File: tracker.py
# Tool: ProgressTrackerTool

"""
Yeh tool user ke progress ko save karta hai.
Jaise user bole "maine apna 3rd workout complete kiya" —
toh yeh us din aur us message ko context me save karta hai.
"""

from openai_agents_sdk import Tool, tool 
from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime
from context import UserSessionContext

# Output model
class ProgressLog(BaseModel):
    date: str
    note: str

@tool(name="ProgressTrackerTool", description="User ke progress updates ko session context mein track karta hai")
class ProgressTrackerTool(Tool):

    async def run(self, input_data: Any, context: UserSessionContext) -> str:
        # Accept string or dict
        if isinstance(input_data, dict):
            note = input_data.get("note", "").strip()
            date = input_data.get("date") or datetime.now().strftime("%Y-%m-%d")
        else:
            note = str(input_data).strip()
            date = datetime.now().strftime("%Y-%m-%d")

        if not note:
            raise ValueError("Progress note required.")

        log = ProgressLog(date=date, note=note)
        
        # ✅ Store in logs
        if hasattr(context, "progress_logs"):
            context.progress_logs.append(log.dict())
        else:
            context.progress_logs = [log.dict()]

        # ✅ Increment workout count
        if hasattr(context, "completed_workouts"):
            context.completed_workouts += 1
        else:
            context.completed_workouts = 1

        # ✅ Return output string (string not object)
        return f"You have completed {context.completed_workouts} workouts so far."
