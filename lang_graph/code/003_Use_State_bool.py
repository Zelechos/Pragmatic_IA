from typing import TypedDict, Annotated
from langgraph.graph import StateGraph
from operator import add


class State(TypedDict):
    age: int
    is_adult: bool
    name: Annotated[str, add]


def have_access(state: State):
    if state["age"] > 18:
        return {"is_adult": True, "name": ", Access Granted"}
    else:
        return {"is_adult": False, "name": ", Access Denied"}


graph = StateGraph(State)

graph.add_node("access", have_access)
graph.set_entry_point("access")
graph.set_finish_point("access")

app = graph.compile()

result = app.invoke({"age": 6, "name": "Argus Aphocraphex"})

print(result)
