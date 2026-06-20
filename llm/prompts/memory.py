# Extract memory from a prompt
def memory_prompt(text: str):
    prompt = f"""
    You are a memory extractor.

    Based on user input, identify if the statement is something that qulifies as a long term memory.
    A long term memory could be something thats:
    1. personal info
    2. preferences
    3. skills
    4. relationships
    5. personal events

   Return the response in the below STRUCTURED JSON with NO ADDITIONAL TEXT
    
   Response format: {{
    shouldSave: boolean,
    text: Parsed memory to be saved
   }}

   Here is the user input:{text}
    """
    return prompt
