class File:
    def run(self):
        with open("example.txt", "r") as file:
            content = file.read()
            return content
            print(content)
