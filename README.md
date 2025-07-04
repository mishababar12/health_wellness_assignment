🤖 Health & Wellness Planner Agent:
This project simulates an AI-powered health assistant without using OpenAI API keys. It mimics the functionality of the OpenAI Agents SDK by using custom tools and agents.

Features:
Analyze user health goals like weight loss or gain
Create personalized 7-day meal plans (vegetarian, keto, etc.)
Suggest weekly workout plans based on fitness level (beginner, intermediate, advanced)
Track user progress and completed workouts
Schedule weekly check-in reminders
Escalate to specialized agents (injury, nutrition, human coach)
Simulate streaming output like real-time chat

Tools Used:
Each tool handles a specific task --

GoalAnalyzerTool	- Analyze goals like "lose 5kg in 2 months"
MealPlannerTool	- Generate 7-day meal plans
WorkoutRecommenderTool	- Recommend workout routines by fitness level
CheckinSchedulerTool	- Create weekly check-in reminders
ProgressTrackerTool	- Log and track user workout progress

Specialized Agents:
InjurySupportAgent -	Handle pain or injury-related queries
NutritionExpertAgent - Help with dietary conditions like diabetes, allergy
EscalationAgent	- Simulate human trainer or escalate complex issues

Project Structure:

health_wellness_agent/
│
├── main_agent.py              # CLI chatbot entry point
├── agent.py                   # Main Health Planner agent
├── context.py                 # Stores user session data
├── guardrails.py              # Input validation rules
│
├── agents/
│   ├── escalation_agent.py
│   ├── injury_support_agent.py
│   ├── nutrition_expert_agent.py
│   └── runner.py              # Simulates streaming responses
│
├── tools/
│   ├── goal_analyser.py
│   ├── meal_planner.py
│   ├── workout_recommender.py
│   ├── scheduler.py
│   └── tracker.py
│
├── utils/
│   └── streaming.py           # (Optional) Prints responses nicely
│
└── README.md
