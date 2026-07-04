from langchain.agents import AgentExecutor, create_tool_calling_agent

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from backend.llm import llm

from backend.tools import calculate_bmi, calculate_bmr, water_intake

tools = [calculate_bmi, calculate_bmr, water_intake]

prompt = ChatPromptTemplate.from_messages(

[

("system", "You are an AI fitness coach. Use tools whenever calculations are needed."),

("human", "{input}"),

MessagesPlaceholder(variable_name="agent_scratchpad"),

]

)

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(

agent=agent,

tools=tools,

verbose=True

)