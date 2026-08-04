from typing import TypedDict, List, Annotated
from operator import add
from langgraph.graph import StateGraph


class State(TypedDict):
    name: Annotated[str, add]
    values: List[int]
    result: int


def sum_values(state: State):
    return {"result": sum(state["values"])}


def response(state: State):
    return {
        "name": ", The sum of your values "
        + str(state["values"])
        + " is: "
        + str(state["result"])
    }


graph = StateGraph(State)

graph.add_node("sum", sum_values)
graph.add_node("response", response)

graph.set_entry_point("sum")
graph.add_edge("sum", "response")
graph.set_finish_point("response")

app = graph.compile()

acii_graph = app.get_graph().draw_ascii()
print(acii_graph)

results = app.invoke({"name": "Argus Aphocraphex", "values": [1, 2, 3, 4, 5, 150]})
print(results["name"])
