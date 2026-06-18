from ddgs import DDGS


class Knowledge:
    def run(self, query: str):
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
            return results
