from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
import random


class State(TypedDict):
    player_name: str
    guesses: List[int]
    attempts: int
    current_attempts: int
    lower_bound: int
    upper_bound: int
    number: int
    magic_number: int
    message: str


# nodes
def setup_node(state: State):
    print(
        "Hello "
        + state["player_name"]
        + ", I'm thinking of a number between "
        + str(state["lower_bound"])
        + " and "
        + str(state["upper_bound"])
        + ".\n"
    )

    return {
        "magic_number": random.randint(state["lower_bound"], state["upper_bound"]),
    }


def guess_node(state: State):
    print("Attempts left: " + str(state["attempts"] - state["current_attempts"]))
    number = int(input("Input a number : "))
    guesses = state["guesses"] + [number]
    type = "higher" if number < state["magic_number"] else "lower"
    return {
        "message": "The number is " + type + " than " + str(number),
        "current_attempts": (state["current_attempts"] + 1),
        "guesses": guesses,
        "number": number,
    }


def route_game(state: State):
    if state["number"] == state["magic_number"]:
        print("You win!")
        return "end"

    if state["attempts"] > state["current_attempts"]:
        print(state["message"])
        return "continue"

    print("You lose!")
    return "end"


# Build graph
graph = StateGraph(State)


graph.add_node("setup", setup_node)
graph.add_node("guess", guess_node)


graph.add_edge(START, "setup")
graph.add_edge("setup", "guess")

graph.add_conditional_edges("guess", route_game, {"continue": "guess", "end": END})

app = graph.compile()

response = app.invoke(
    {
        "player_name": "Argus Aphocraphex",
        "lower_bound": 1,
        "upper_bound": 100,
        "attempts": 10,
        "guesses": [],
        "current_attempts": 0,
    }
)

print(response)
