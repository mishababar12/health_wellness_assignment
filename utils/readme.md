# Health & Wellness Planner Agent

An AI-powered digital health assistant built using OpenAI Agents SDK.

## 💡 Features

- Multi-turn conversation to understand user health goals
- Structured goal analysis (e.g., "lose 5kg in 2 months")
- Personalized 7-day meal plans (e.g., vegetarian, keto)
- Workout plans based on experience (beginner to advanced)
- Weekly progress check-ins with reminders
- Progress tracking with session history
- Specialized agents for injuries, dietary conditions, or escalation to human coach
- Real-time chatbot streaming using `Runner.stream()`

## 🛠 Tools Used

- `GoalAnalyzerTool`
- `MealPlannerTool`
- `WorkoutRecommenderTool`
- `CheckinSchedulerTool`
- `ProgressTrackerTool`

## 🤝 Specialized Agents

- `InjurySupportAgent`
- `NutritionExpertAgent`
- `EscalationAgent`

## 📦 Project Structure

health_wellness_agent/
├── main.py
├── agent.py
├── context.py
├── guardrails.py
├── tools/
├── agents/
├── utils/
└── README.md