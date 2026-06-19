# Get speech from knowledge to be played on audio
def speech_prompt(text:str):
    prompt = f"""
    You are a text to speech converting agent.

    You'll receive a text that's supposed to be spoken to the user as a response to their query. 

    Parse the text in a format that could be spoken to the user. 
    
    Try to keep it short.

    Text: {text}
    """
    return prompt