import json
from llm.ollama import ask
from tools.registry import Tools

while True:
    user_input = input("Hey! What are you looking for today?")

    prompt = f"""
        You are a tool router working with the following tools:
        
        - youtube
            :for reuqets that involve playing music or videos

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
    """

    response = ask(prompt)
    print(response)

    command = json.loads(response)
    tool = Tools[command["tool"]]
    tool.run(command["input"])
