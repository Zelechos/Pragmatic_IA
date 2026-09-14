from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, START, END
import random


class State(TypedDict):
    name: str
    message: str
    numbers: List[int]
    counter: int
    quantity: int


# Define graphs
def greeting_node(state: State):
    return {"message": "Hello " + state["name"] + " how is your going? ", "counter": 0}


def random_node(state: State):
    state["numbers"].append(random.randint(1, 100))
    return {
        "numbers": state["numbers"],
        "counter": state["counter"] + 1,
    }


def condition_node(state: State):
    return "increment" if state["counter"] < state["quantity"] else "add"


# Build Graph
graph = StateGraph(State)

graph.add_node("greet", greeting_node)
graph.add_node("random", random_node)
graph.add_node("condition", condition_node)

graph.add_edge(START, "greet")
graph.add_edge("greet", "random")
graph.add_conditional_edges(
    "random", condition_node, {"increment": "random", "end": END}
)

app = graph.compile()

response = app.invoke({"name": "Argus Aphocraphex", "quantity": 34, "numbers": []})

print(
    response["message"]
    + "\nThe random numbers are: "
    + str(response["numbers"])
    + "\nThe quantity is : "
    + str(response["quantity"])
)
