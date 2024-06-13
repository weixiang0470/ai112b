from env import *
from mylangchain import *

llm = ChatGroq(temperature=1, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")

tools = [TavilySearchResults(max_results=2)]
#tools = load_tools(["serpapi", "llm-math"], llm=llm)

#Create agent
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Make sure to use the tavily_search_results_json tool for information.",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# Construct the Tools agent
agent = create_tool_calling_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)
#response = agent_executor.invoke({"input": "請問National Quemoy University有哪些教授？"})
#print(response['output'])
input_text = input('>>> ')
while input_text.lower() != 'bye':
    if input_text:
        response = agent_executor.invoke({
            'input': input_text,
        })
        print(response['output'])
    input_text = input('>>> ')