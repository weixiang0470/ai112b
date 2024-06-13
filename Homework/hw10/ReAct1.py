from env import *
from mylangchain import *

llm = ChatGroq(temperature=1, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("請問National Quemoy University有哪些教授？")