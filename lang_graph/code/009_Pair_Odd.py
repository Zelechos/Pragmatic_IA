from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, START, END
from operator import add
import random


class State(TypedDict):
    number: int
    message: Annotated[str, add]


def odd_node(state: State):
    return {"message": "The number is " + str(state["number"]) + " is odd!"}


def pair_node(state: State):
    return {"message": "The number is " + str(state["number"]) + " is pair!"}


def pair_or_odd(state: State):
    return "pair" if state["number"] % 2 == 0 else "odd"


def default_node(state: State):
    return state


graph = StateGraph(State)

graph.add_node("odd_node", odd_node)
graph.add_node("pair_node", pair_node)
graph.add_node("router", default_node)

graph.add_edge(START, "router")

# Conditional
graph.add_conditional_edges(
    "router", pair_or_odd, {"pair": "pair_node", "odd": "odd_node"}
)

graph.add_edge("pair_node", END)
graph.add_edge("odd_node", END)


app = graph.compile()

ascii_art = app.get_graph().draw_ascii()
print(ascii_art)

ramdom_100_numbers = [
    app.invoke({"number": x})["message"] for x in range(1, random.randint(100, 1001))
]

print(*ramdom_100_numbers, sep="\n")
