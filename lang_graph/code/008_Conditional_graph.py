from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    number1: int
    number2: int
    operator: str
    result: int


def add(state: State):
    return {"result": state["number1"] + state["number2"]}


def sub(state: State):
    return {"result": state["number1"] - state["number2"]}


def mul(state: State):
    return {"result": state["number1"] * state["number2"]}


def div(state: State):
    if state["number1"] > state["number2"]:
        return "normal_division_operation"
    else:
        return "inverse_division_operation"


def normal_division(state: State):
    return {"result": state["number1"] / state["number2"]}


def inverse_division(state: State):
    return {"result": state["number2"] / state["number1"]}


def router_operation(state: State):
    if state["operator"] == "+":
        return "add_operation"
    elif state["operator"] == "-":
        return "sub_operation"
    elif state["operator"] == "*":
        return "mul_operation"
    elif state["operator"] == "/":
        return "div_operation"


def router_node(state: State):
    return state


graph = StateGraph(State)


graph.add_node("add", add)
graph.add_node("sub", sub)
graph.add_node("mul", mul)
graph.add_node("div", router_node)
graph.add_node("nomal_div", normal_division)
graph.add_node("inverse_div", inverse_division)
graph.add_node("router", router_node)

graph.add_edge(START, "router")


graph.add_conditional_edges(
    "router",
    router_operation,
    {
        "add_operation": "add",
        "sub_operation": "sub",
        "mul_operation": "mul",
        "div_operation": "div",
    },
)

graph.add_conditional_edges(
    "div",
    div,
    {
        "normal_division_operation": "nomal_div",
        "inverse_division_operation": "inverse_div",
    },
)

graph.add_edge("add", END)
graph.add_edge("sub", END)
graph.add_edge("mul", END)
graph.add_edge("nomal_div", END)
graph.add_edge("inverse_div", END)

app = graph.compile()

ascii_art = app.get_graph().draw_ascii()
print(ascii_art)

response_in = State(number1=10, number2=5, operator="+")
response = app.invoke({"number1": 10, "number2": 5, "operator": "/"})

print(response["result"])
print(app.invoke(response_in))
