def tool_identifier_prompt(user_input:str):
    prompt = f"""
        You are a tool router working with the following tools:
        
        - youtube
            :for requests that involve playing music or videos
        - knowledge
            :for requests that involve user asking for some information that could be fetched from the web

        Your task is to identify if the user is asking for access to the above mentioned tools.

        If yes, then return a STRICT JSON as mentioned below without anything additional:
        {{
            tool: Tool name from the list above or null if no tool could be identified
            input: Input that the tool might need to complete user request
        }}

        Example Input: Play me good life from fast and furious
        Example Output: {{
            tool: youtube,
            input: moon river by andy williams
        }}

        Here is the user request: {user_input}

        IMPORTANT: DO NOT SEND ANYTHING ELSE OTHER THAN THE VALID JSON MENTIONED ABOVE.
    """
    return prompt