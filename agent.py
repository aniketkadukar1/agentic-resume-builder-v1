import os
from dotenv import load_dotenv

from typing import Annotated, Literal
from typing_extensions import TypedDict

from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import MemorySaver

from langchain_groq import ChatGroq
from tools import get_job, get_resume

load_dotenv()

tools = [get_job, get_resume]

llm = ChatGroq(model="qwen-2.5-32b").bind_tools(tools)

def expert(state: MessagesState):
    system_message="""
    You are a resume expert. You are tasked with improving the user resume based on a job description.
    You can access the resume and job data using the provided tools.

    You must NEVER provide information that the user does not have.
    These include, skills or experiences that are not in the resume. Do not make things up.
    """

    messages = state["messages"]
    response = llm.invoke([system_message] + messages)

    return {"messages": [response]}


tool_node = ToolNode(tools)

def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:
        return "tools"
    return END

graph = StateGraph(MessagesState)

graph.add_node("expert", expert)
graph.add_node("tools", tool_node)

graph.add_edge(START, "expert")
graph.add_conditional_edges("expert", should_continue)

graph.add_edge("tools", "expert")

checkpointer = MemorySaver()

app = graph.compile(checkpointer=checkpointer)

while True:
    user_input = input(">> ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = app.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config={"configurable": {"thread_id": 1}}
    )

    # output the response
    print(response["messages"][-1].content)