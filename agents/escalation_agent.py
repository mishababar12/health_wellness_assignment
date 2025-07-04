
# File: escalation_agent.py
# Agent: EscalationAgent

"""
Yeh agent tab active hota hai jab user bole "I want to talk to a real trainer".
Yeh batata hai ke human trainer aap se contact karega.
"""

from openai_agents_sdk import Agent, agent 
from pydantic import BaseModel

class EscalationNote(BaseModel):
    message: str

@agent(name="EscalationAgent", description="User agar human trainer se baat karna chahta hai to escalate karta hai")
class EscalationAgent(Agent):

    async def run(self, input_text: str) -> EscalationNote:
        return EscalationNote(
            message="Thanks for your request. A human trainer will be notified and will get in touch with you shortly."
        )
