"""
Context manager
"""
class DatabaseConnection:
    """
    Simulate a database connection with context management
    """
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        """Establishing connection"""
        self.connected = True
        print(f"Connected to database `{self.db_name}` .")
        return self 

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the connection"""
        self.connected = False 
        print(f"Disconnected from database `{self.db_name}`")

        if exc_type:
            print("A Exception occured")
        return True  
        
with DatabaseConnection("ExampleDB") as db:
    print(f"Is Connected:{db.connected}")
