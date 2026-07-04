from backend.graph import chat


def generate_diet(user):

    prompt = f"""
Create a detailed 7-day diet plan.

User Profile

Goal: {user.goal}
Age: {user.age}
Gender: {user.gender}
Weight: {user.weight}
Height: {user.height}
Activity Level: {user.activity_level}

Include:

- Breakfast
- Morning Snack
- Lunch
- Evening Snack
- Dinner
- Calories
- Protein
- Water Intake

Return in markdown format.
"""

    return chat(user, prompt)