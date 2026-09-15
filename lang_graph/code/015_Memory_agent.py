import os
from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]


llm = ChatOpenAI(model="gpt-4o")


def process(state: AgentState):
    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    print(f"\n AI : {response.content}")
    return {"messages": state["messages"]}


graph = StateGraph(AgentState)

graph.add_node("process", process)

graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

# Read a memory.txt and put the text in conversation_history
conversation_history = []
if os.path.exists("memory.txt"):
    with open("memory.txt", "r") as file:
        conversation_history = []
        for line in file:
            if "You: " in line:
                conversation_history.append(HumanMessage(content=line.strip("You: ")))
            elif "AI: " in line:
                conversation_history.append(AIMessage(content=line.strip("AI: ")))

user_input = input("You : ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))

    result = agent.invoke({"messages": conversation_history})
    # print(result["messages"])

    conversation_history = result["messages"]
    user_input = input("You : ")

# Memory of Agent in File
with open("memory.txt", "w") as file:
    file.write("Your conversation history: \n")
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n\n")

    file.write("End of Conversation")


print("Conversation saved to memory.txt")
