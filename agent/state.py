from typing import TypedDict, Optional

class EmailState(TypedDict):
    email_content: str
    category: Optional[str]
    research_info: Optional[str]
    draft_responce: Optional[str]