import requests

class WebSearch:
    def __init__(self, query):
        self.query = query

    def perform_search(self):
        # Example of online search functionality, replace with actual API or web scraping logic
        print(f"Searching for: {self.query}")
        # This is a placeholder for real search implementation
        return f"Results for: {self.query}"

if __name__ == '__main__':
    search = WebSearch('example query')
    print(search.perform_search())