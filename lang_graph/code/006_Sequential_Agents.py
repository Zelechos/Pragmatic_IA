from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph


class State(TypedDict):
    message: Annotated[str, add]
    name: str
    email: str
    age: int


# First node
def gretting_node(state: State):
    return {"message": "Hello " + state["name"] + " how is your going? "}


# Second Node
def age_node(state: State):
    return {"message": "Can you tell me " + str(state["age"]) + " is your age? "}


# Third Node
def email_node(state: State):
    return {"message": "And your email is: " + state["email"]}


graph = StateGraph(State)

graph.add_node("greeting", gretting_node)
graph.add_node("age", age_node)
graph.add_node("email", email_node)

graph.set_entry_point("greeting")
graph.add_edge("greeting", "age")
graph.add_edge("age", "email")
graph.set_finish_point("email")

app = graph.compile()

ascii_art = app.get_graph().draw_ascii()
print(ascii_art)

result = app.invoke(
    {"name": "Argus Aphocraphex", "age": 16, "email": "argusaphocraphex@me.com"}
)

print(result["message"])
