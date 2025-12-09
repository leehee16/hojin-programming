from dotenv import load_dotenv
load_dotenv

from typing import Annotated
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI

from langgraph.graph.message import add_messages #메세지를 두개받아서 하나로 반환하는 함수
from langchain_core.messages import AnyMessage 
from langgraph.graph import START,END, StateGraph


class AgentState(TypedDict):
    message: list[Annotated[AnyMessage,add_messages]]


def generate(state: AgentState) -> AgentState:
    llm = ChatOpenAI(model='gpt-4o-mini')
    messages = state['message']
    ai_messages = llm.invoke(messages)
    return {'message': [ai_messages]}

if __name__ == '__main__':
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node('generate', generate)
    graph_builder.add_edge(START,'generate')
    graph_builder.add_edge('generate', END)
    graph = graph_builder.compile()

    

