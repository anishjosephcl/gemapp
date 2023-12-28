from langchain.agents import initialize_agent
from model.geminimodel import get_llm_model
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import Tool
from langchain.tools import BaseTool
import random

search = DuckDuckGoSearchRun()
# defining a search  tool
duck_tool = Tool(
        name = "search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions"
    )


def meaning_of_life(input=""):
    return 'The meaning of life is 42 if rounded but is actually 42.17658'

life_tool = Tool(
    name='Meaning of Life',
    func= meaning_of_life,
    description="Useful for when you need to answer questions about the meaning of life. input should be MOL "
)

def random_num(input=""):
    return random.randint(0,3)

random_tool = Tool(
    name='Random number',
    func= random_num,
    description="Useful for when you need to get a random number. input should be 'random'"
)
gmodel = get_llm_model()

tools = [duck_tool, random_tool, life_tool]

# conversational agent memory
memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=3,
    return_messages=True
)

# create our agent
conversational_agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=gmodel,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=memory
)

##conversational_agent("What time is it in London?")
conversational_agent("Can you give me a random number?")