
# File: injury_support_agent.py
# Agent: InjurySupportAgent

"""
Yeh agent un logon ke liye hai jinko chot ya pain hai (jaise 'knee pain').
Yeh suggest karta hai ke aapko kya karna chahiye, aur kya avoid karna hai.
"""

from openai_agents_sdk import Agent, agent
from pydantic import BaseModel

class InjurySupportOutput(BaseModel):
    message: str

@agent(name="InjurySupportAgent", description="Injury ya restriction hone par guidance deta hai")
class InjurySupportAgent(Agent):

    async def run(self, input_text: str) -> InjurySupportOutput:
        return InjurySupportOutput(
            message="Thanks for informing. Please avoid high-impact exercises. Focus on gentle stretches and consult a physiotherapist if pain continues."
        )
