from typing import TypedDict, Dict
from langgraph.graph import StateGraph
from IPython.display import Image, display


# This is normal python
class AgentState(TypedDict):  # Our State Squema
    message: str


# first Node
def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds a greeting message to the state"""
    state["message"] = "Hello " + state["message"] + " how is your going?"
    return state


# Now is the time to use LangGraph
graph = StateGraph(AgentState)

# Add node
graph.add_node("greeting", greeting_node)

graph.set_entry_point("greeting")  # Set the entry point
graph.set_finish_point("greeting")  # Set the finish point

# Compile the Graph
app = graph.compile()


# To see a diagram of graph
# display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"message": "Argus Aphocraphex"})

print(result["message"])
