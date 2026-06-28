class Filemanager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        # Open a file
        self.file = open(self.filename, self.mode)
        print(f"Opening a file {self.filename}")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the file
        self.file.close()
        print(f"Closing file {self.filename}")
        # Handle excpetions (if any) here
        if exc_type:
            print(f"An excpetion occured: {exc_val}")
        return True

if __name__ == "__main__":
    with Filemanager("example.txt", "w") as file:
        file.write("Hello, Direk!")
        print("File written successfully")

    with Filemanager("example.txt", "r") as file:
        content = file.read()
        print(f"File content: {content}")