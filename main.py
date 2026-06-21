import json
from llm.ollama import ask

from tools.registry import Tools
from speech.record import record_audio
from speech.transcribe import transcribe
from speech.speak import speak
from llm.prompts.tool_identifier import tool_identifier_prompt
from llm.prompts.speech import speech_prompt

while True:
    # user_input = input("Hey! What are you looking for today?")
    audio_file = record_audio()

    user_input = transcribe(audio_file)

    prompt = tool_identifier_prompt(user_input)

    response = ask(prompt)
    # print(response)

    command = json.loads(response)
    tool = Tools[command["tool"]]
    output = tool.run(command["input"])
    match command["tool"]:
        case "knowledge":
            speech_response = ask(speech_prompt(output[0]["summary"]))
            print(speech_response)
            speak(output[0]["summary"])
            break
        case "youtube":
            Tools["youtube"].run(command["message"])
