# Extract file content
def file_content_prompt(
    file_content: str, question="What is the summary of this file?"
):
    prompt = f"""
    You are a file content reader.

    Take this file content: {file_content}
    Answer this question: {question}

    Give a presise and short answer.
    """
    return prompt
