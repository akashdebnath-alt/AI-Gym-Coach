from backend.graph import chat


def generate_workout(user):

    prompt = f"""
Create a detailed 7-day workout plan.

Requirements:
- Goal: {user.goal}
- Experience: {user.experience_level}
- Equipment: {user.available_equipment}
- Activity Level: {user.activity_level}
- Age: {user.age}
- Weight: {user.weight}
- Height: {user.height}

The workout should include:

- Day wise split
- Exercises
- Sets
- Reps
- Rest time
- Cardio
- Tips

Return in markdown format.
"""

    return chat(user, prompt)