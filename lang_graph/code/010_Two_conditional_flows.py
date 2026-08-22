from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from operator import add


# Create a state of graph
class State(TypedDict):
    number1: int
    number2: int
    number3: int
    number4: int
    number5: int
    operation1: str
    operation2: str
    operation3: str
    response: Annotated[str, add]


# Create a nodes of graph
def add_node(state: State):
    sum = str(state["number1"] + state["number2"])
    return {
        "response": "\nThe addition of : "
        + str(state["number1"])
        + " + "
        + str(state["number2"])
        + " = "
        + sum
    }


def sub_node(state: State):
    sub = str(state["number1"] - state["number2"])
    return {
        "response": "\nThe subtraction of : "
        + str(state["number1"])
        + " - "
        + str(state["number2"])
        + " = "
        + sub
    }


def mult_node(state: State):
    mult = str(state["number3"] * state["number4"])
    return {
        "response": "\nThe multiplication of : "
        + str(state["number3"])
        + " * "
        + str(state["number4"])
        + " = "
        + mult
    }


def div_node(state: State):
    div = str(state["number3"] / state["number4"])
    return {
        "response": "\nThe division of : "
        + str(state["number3"])
        + " / "
        + str(state["number4"])
        + " = "
        + div
    }


def factorial_node(state: State):
    aux = state["number5"]
    for i in range(1, aux):
        aux = aux * i
    fact = str(aux)
    return {
        "response": "\nThe factorial of : " + str(state["number5"]) + "!" + " = " + fact
    }


def square_node(state: State):
    square = str(state["number5"] ** 2)
    return {"response": "\nThe square of : " + str(state["number5"]) + " = " + square}


# Operations
def operation1_node(state: State):
    return "addition" if state["operation1"] == "+" else "subtraction"


def operation2_node(state: State):
    return "multiplication" if state["operation2"] == "*" else "division"


def operation3_node(state: State):
    return "factorial" if state["operation3"] == "!" else "square"


# Build the Graph
graph = StateGraph(State)

# Add nodes
graph.add_node("addition", add_node)
graph.add_node("subtraction", sub_node)
graph.add_node("multiplication", mult_node)
graph.add_node("division", div_node)
graph.add_node("factorial", factorial_node)
graph.add_node("square", square_node)
graph.add_node("route", lambda state: {})
graph.add_node("route1", lambda state: {})

# Add Conditional edges
graph.add_conditional_edges(
    START, operation1_node, {"addition": "addition", "subtraction": "subtraction"}
)

graph.add_edge("addition", "route")
graph.add_edge("subtraction", "route")

graph.add_conditional_edges(
    "route",
    operation2_node,
    {"multiplication": "multiplication", "division": "division"},
)

graph.add_edge("multiplication", "route1")
graph.add_edge("division", "route1")

graph.add_conditional_edges(
    "route1",
    operation3_node,
    {"factorial": "factorial", "square": "square"},
)

graph.add_edge("factorial", END)
graph.add_edge("square", END)


app = graph.compile()

ascii_view = app.get_graph().draw_ascii()
print(ascii_view)

rest = app.invoke(
    {
        "number1": 1,
        "number2": 3,
        "number3": 5,
        "number4": 4,
        "number5": 6,
        "operation1": "+",
        "operation2": "*",
        "operation3": "!",
    }
)

print(rest["response"])
