# File: main.py
# Purpose:Yeh file user aur HealthWellnessPlannerAgent ke darmiyan CLI par conversation handle karti hai.

"""
In this file:
- User se input liya jaega (e.g. health goal, diet, etc.)
- Yeh input `Runner.stream(...)` ko bhej diya jaega
- Agent ka response step-by-step print hoga (streaming effect)

"""

import asyncio
from agents.runner import Runner
from agent import HealthWellnessPlannerAgent
from context import UserSessionContext
from utils.streaming import stream_output  # Optional: custom streamer

# Sample context
user_context = UserSessionContext(
    name="Misha", uid=1
)

# Simple CLI interface
async def main():
    print("🤖 Welcome to the Health & Wellness Planner Agent!")
    print("💬 Type your health goal or preference below (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        print("Agent:")
        async for step in Runner.stream(
            starting_agent=HealthWellnessPlannerAgent(),
            input=user_input,
            context=user_context
        ):
            print(step.pretty_output)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
