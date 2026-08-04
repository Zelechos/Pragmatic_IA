from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph


class State(TypedDict):
    name: Annotated[str, add]
    score: int
    passed: bool


def student_passed(state: State):
    passed = state["score"] >= 60
    return {
        "passed": passed,
        "name": (
            ", Congratulations! You passed the exam."
            if passed
            else ", Don't  give up!  Keep studying."
        ),
    }


graph = StateGraph(State)

graph.add_node("passed", student_passed)
graph.set_entry_point("passed")
graph.set_finish_point("passed")

app = graph.compile()

ascii_art = app.get_graph().draw_ascii()
print(ascii_art)


result1 = app.invoke({"name": "Alice", "score": 85})

print(result1)

result2 = app.invoke({"name": "John", "score": 40})

print(result2)
