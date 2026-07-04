from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from backend.llm import llm
from backend.tools import (
    calculate_bmi,
    calculate_bmr,
    water_intake,
)
from backend.rag.retriever import get_retriever

memory = InMemorySaver()

tools = [
    calculate_bmi,
    calculate_bmr,
    water_intake,
]

graph = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,
    prompt="""
You are FitGenie, an AI Gym Coach.

Use tools whenever calculations are required.

Use the provided fitness knowledge whenever it is relevant.

Never guess BMI, BMR or Water Intake.
Always use the available tools.
"""
)

retriever = get_retriever()


def chat(user, question):

    profile = f"""
User Profile

Name: {user.name}
Age: {user.age}
Gender: {user.gender}
Height: {user.height} cm
Weight: {user.weight} kg
Goal: {user.goal}
Activity Level: {user.activity_level}
Experience Level: {user.experience_level}
Medical Conditions: {user.medical_conditions}
Available Equipment: {user.available_equipment}
"""

    docs = retriever.invoke(question)

    knowledge = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    response = graph.invoke(
        {
            "messages": [
                {
                    "role": "system",
                    "content": profile,
                },
                {
                    "role": "system",
                    "content": f"Fitness Knowledge:\n\n{knowledge}",
                },
                {
                    "role": "user",
                    "content": question,
                },
            ]
        },
        config={
            "configurable": {
                "thread_id": str(user.id)
            }
        }
    )

    content = response["messages"][-1].content

    if isinstance(content, list):
        answer = ""
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                answer += item.get("text", "")
        return answer

    return content