
# File: guardrails.py
# Purpose: User ke input ko validate (check) karna

"""
Yeh file check karti hai ke user ka input sahi format me hai ya nahi:

  validate_goal_input(goal_text)
    Check karta hai ke goal sahi format me hai ya nahi
    Jaise: "lose 5kg in 2 months"

  validate_diet_input(diet)
    Check karta hai ke diet type valid hai ya nahi
    (vegetarian, keto, diabetic, default)

  validate_experience_level(level)
    Check karta hai ke user ka workout level valid hai ya nahi
    (beginner, intermediate, advanced)

  validate_date_format(date_str)
    Check karta hai ke date format sahi hai ya nahi
    Jaise: "2025-07-01"

Ye file input filtering & safety ke liye kaafi important hoti hai — agar ye check na karein,
toh galat input pe tool ya agent crash kar sakta hai.

"""

import re

def validate_goal_input(goal_text: str) -> bool:
    pattern = r"(lose|gain)\s+(\d+\.?\d*)\s*(kg|lbs)\s+in\s+(\d+\s*(days|weeks|months))"
    return bool(re.search(pattern, goal_text.lower()))

def validate_diet_input(diet: str) -> bool:
    valid_diets = ["vegetarian", "keto", "diabetic", "default"]
    return diet.lower() in valid_diets

def validate_experience_level(level: str) -> bool:
    return level.lower() in ["beginner", "intermediate", "advanced"]

def validate_date_format(date_str: str) -> bool:
    try:
        from datetime import datetime
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
