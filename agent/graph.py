from langgraph.graph import StateGraph, END
from state import EmailState
from nodes import (
    read_email_node, 
    categorize_email_node, 
    research_info_node, 
    draft_response_node
)

def route_to_research(state: EmailState):
    if state['category'] in ["bug", "question"]:
        return "research"
    else:
        return "draft"

workflow = StateGraph(EmailState)

workflow.add_node("read_email", read_email_node)
workflow.add_node("categorize", categorize_email_node)
workflow.add_node("research", research_info_node)
workflow.add_node("draft", draft_response_node)

workflow.set_entry_point("read_email")
workflow.add_edge("read_email", "categorize")

workflow.add_conditional_edges(
    "categorize",
    route_to_research,
    {
        "research": "research",
        "draft": "draft"
    }
)

workflow.add_edge("research", "draft")
workflow.add_edge("draft", END)

app = workflow.compile()