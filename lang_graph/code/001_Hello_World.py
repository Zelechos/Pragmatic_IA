from typing import TypedDict, Dict
from langgraph.graph import StateGraph


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

# Draw the Graph
ascii_art = app.get_graph().draw_ascii()
print(ascii_art)

result = app.invoke({"message": "Argus Aphocraphex"})

print(result["message"])
