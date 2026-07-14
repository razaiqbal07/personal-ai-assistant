from pathlib import Path
from pypdf import PdfReader

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
                print("Found:", path)

                if not path.is_file():
                    continue

                # Read PDF files
                if path.suffix.lower() == ".pdf":
                    reader = PdfReader(path)
                    content = "\n".join(
                        page.extract_text() or ""
                        for page in reader.pages
                    )
                    return content

                # Read text files
                with open(path, "r", encoding="utf-8") as file:
                    return file.read()

        return None