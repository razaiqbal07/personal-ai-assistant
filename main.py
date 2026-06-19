import json
from llm.ollama import ask
from tools.registry import Tools
from speech.record import record_audio
from speech.transcribe import transcribe


while True:
    # user_input = input("Hey! What are you looking for today?")
    audio_file = record_audio()

    user_input = transcribe(audio_file)

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

    response = ask(prompt)
    print(response)

    command = json.loads(response)
    tool = Tools[command["tool"]]
    output = tool.run(command["input"])
    print(output)
