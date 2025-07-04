# File: scheduler.py
# Tool: CheckinSchedulerTool

"""
Yeh tool weekly check-in reminders set karta hai.
Agar user bole "start from 2025-07-01", toh yeh har week ka ek reminder banata hai.
"""

from openai_agents_sdk import Tool, tool
from pydantic import BaseModel
from typing import List
import datetime

# Output model
class CheckinSchedule(BaseModel):
    reminders: List[str]

@tool(name="CheckinSchedulerTool", description="User ke weekly check-in schedule ko manage karta hai")
class CheckinSchedulerTool(Tool):

    async def run(self, start_day: str) -> CheckinSchedule:
        # 4 weekly reminders
        try:
            day = datetime.datetime.strptime(start_day, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date format should be YYYY-MM-DD")

        reminders = []
        for i in range(4):  # 4 weeks
            checkin_day = day + datetime.timedelta(weeks=i)
            reminders.append(f"Week {i+1} Check-in: {checkin_day.strftime('%A, %d %B %Y')}")

        return CheckinSchedule(reminders=reminders)
