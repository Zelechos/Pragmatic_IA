from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, START, END
from operator import add
import random


class State(TypedDict):
    number: int
    message: Annotated[str, add]


def odd_node(state: State):
    return {"message": "The number is " + str(state["number"]) + " is odd!"}


def even_node(state: State):
    return {"message": "The number is " + str(state["number"]) + " is even!"}


def even_or_odd(state: State):
    return "even" if state["number"] % 2 == 0 else "odd"


graph = StateGraph(State)

graph.add_node("odd_node", odd_node)
graph.add_node("even_node", even_node)

# Conditional
graph.add_conditional_edges(
    START, even_or_odd, {"even": "even_node", "odd": "odd_node"}
)

graph.add_edge("even_node", END)
graph.add_edge("odd_node", END)


app = graph.compile()

ascii_art = app.get_graph().draw_ascii()
print(ascii_art)

ramdom_100_numbers = [
    app.invoke({"number": x})["message"] for x in range(1, random.randint(100, 1001))
]

print(*ramdom_100_numbers, sep="\n")
