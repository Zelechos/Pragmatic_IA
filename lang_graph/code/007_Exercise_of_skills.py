from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph
from operator import add


class State(TypedDict):
    name: str
    age: int
    skills: List[str]
    message: Annotated[str, add]


# First Node
def greeting_node(state: State):
    return {"message": state["name"] + ", welcome to the System!"}


# Second Node
def years_node(state: State):
    return {"message": " You are " + str(state["age"]) + " years old!"}


# Third Node
def skills_node(state: State):
    return {"message": " You have skills in: " + ", ".join(state["skills"])}


graph = StateGraph(State)

graph.add_node("greeting", greeting_node)
graph.add_node("years", years_node)
graph.add_node("skills", skills_node)

# Structured a graph
graph.set_entry_point("greeting")
graph.add_edge("greeting", "years")
graph.add_edge("years", "skills")
graph.set_finish_point("skills")

app = graph.compile()

ascii_art = app.get_graph().draw_ascii()
print(ascii_art)


result = app.invoke(
    {
        "name": "Argus Aphocraphex",
        "age": 16,
        "skills": ["Python", "LangGraph", "Pytorch"],
    }
)

print(result["message"])
