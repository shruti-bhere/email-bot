from graph import app

if __name__ == "__main__":
    print("### Starting Local Email Bot ###")
    
    # Example Email Input
    email_input = {
        # This text doesn't trigger "bug" or "question" logic, so it becomes "other"
        "email_content": "Hello, just saying hi!" 
    }

    try:
        result = app.invoke(email_input)
        
        print("\n\n################ RESULT ################")
        print(f"CATEGORY: {result.get('category')}")
        
        # SAFE PRINT: If 'research_info' is missing, print "None" instead of crashing
        print(f"RESEARCH: {result.get('research_info', 'Skipped')}") 
        
        print("-" * 30)
        print(f"FINAL DRAFT:\n{result.get('draft_responce')}")
        print("########################################")
        
    except Exception as e:
        print(f"An error occurred: {e}")