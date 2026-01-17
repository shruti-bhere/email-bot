from state import EmailState

# --- NO LLM IMPORT NEEDED ---
# We are simulating the AI logic with Python code

def read_email_node(state: EmailState):
    """
    Simulates reading an email.
    """
    print(f"\n--- Reading Email ---")
    return state

def categorize_email_node(state: EmailState):
    """
    SIMULATED AI: Categorizes based on keywords.
    """
    print("--- Categorizing Email (Mock Mode) ---")
    email_text = state['email_content'].lower()
    
    # Simple keyword logic instead of AI
    if "error" in email_text or "crash" in email_text:
        category = "bug"
    elif "how" in email_text or "help" in email_text:
        category = "question"
    else:
        category = "other"
    
    print(f"Detected Category: {category}")
    return {"category": category}

def research_info_node(state: EmailState):
    """
    Fetches fake research data.
    """
    print("--- Researching Information ---")
    category = state['category']
    
    if category == "bug":
        info = "Known Issue #55: Reset your cache to fix the crash."
    elif category == "question":
        info = "Documentation: Go to Settings > Export to download data."
    else:
        info = "No specific research needed."
        
    return {"research_info": info}

def draft_response_node(state: EmailState):
    """
    SIMULATED AI: Combines templates to make a reply.
    """
    print("--- Drafting Response (Mock Mode) ---")
    category = state['category']
    research = state.get('research_info', "")
    
    # Template-based response
    draft = f"""
    Subject: Re: Your {category}
    
    Dear User,
    
    Thank you for contacting us. Regarding your {category}:
    
    {research}
    
    Let us know if this helps!
    
    Best,
    Support Bot
    """
    
    return {"draft_responce": draft}