from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from operator import add


# Create a state of graph
class State(TypedDict):
    number1: int
    response: Annotated[str, add]


# Create a nodes of graph
def add_node(state: State):
    sum = state["number1"] + 1
    return {"response": str(state["number1"]) + ", ", "number1": sum}


def route_node(state: State):
    return "end" if state["number1"] > 100 else "add"


# Build the Graph
graph = StateGraph(State)

# Add nodes
graph.add_node("add", add_node)
graph.add_node("route", route_node)

graph.add_edge(START, "add")
graph.add_conditional_edges("add", route_node, {"add": "add", "end": END})

app = graph.compile()

rest = app.invoke(
    {
        "number1": 1,
    }
)

print("response -> " + rest["response"])
