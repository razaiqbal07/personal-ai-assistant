from pathlib import Path

filename = "report.pdf"

locations = [
    Path.home() / "Downloads",
    Path.home() / "Documents",
    Path.home() / "Desktop",
]


class File:
    def run(self, filename: str):
        print(filename)
        for location in locations:
            for path in location.rglob(filename):
                print("pathhh", path)
                if path:
                    with open(path, "r") as file:
                        content = file.read()
                        return content
