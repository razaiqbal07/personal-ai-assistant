from ddgs import DDGS


class Knowledge:
    def run(self, query: str):
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
        normalized = []

        for result in results:
            normalized.append({
                "title": result.get("title", ""),
                "summary": result.get("body", ""),
                "url": result.get("href", "")
            })
        return normalized
