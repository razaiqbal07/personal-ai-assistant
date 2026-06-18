import webbrowser
from urllib.parse import quote


class YoutubeTool:
    def run(self, query: str):
        url = "https://www.youtube.com/results?search_query=" f"{quote(query)}"
        webbrowser.open(url)

        return f"Opened YouTube for {query}"
