
# File: runner.py
# Purpose: Yeh file ek helper class `Runner` define karti hai jo agent se response lene aur usko stream 
# (step by step) karne ke liye use hoti hai.

"""
Function: stream()
- `starting_agent.run(...)` ko call karta hai.
- Uska output `Step` object me wrap karta hai.
- Aur `yield` karke streaming style me wapas bhejta hai.

"""



class Runner:
    @staticmethod
    async def stream(starting_agent, input, context):
        class Step:
            def __init__(self, output):
                self.pretty_output = output
        # Example: call the agent's run method and yield the result
        result = await starting_agent.run(input, context)
        yield Step(str(result))