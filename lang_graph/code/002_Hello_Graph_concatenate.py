from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph


# 1. Create a state squema
class State(TypedDict):
    name: Annotated[str, add]


# 2. Create a node definition
def concatenate(state: State) -> State:
    return {
        "name": ", you're doing an amazing job  learning LangGraph"
    }  # Return a Partial state update


# 3. Create a Graph
graph = StateGraph(State)

# 4. Add node
graph.add_node("concatenate", concatenate)

# 5. Set Entry & End point
graph.set_entry_point("concatenate")
graph.set_finish_point("concatenate")

# 6. Compile the graph
app = graph.compile()

# 7. Invoke the app
result = app.invoke({"name": "Bob"})

print(result["name"])
