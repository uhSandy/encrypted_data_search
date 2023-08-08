import pickle

class SearchClass:
    def __init__(self):
        pass

    def search_data(self, data):
        # Add your code to process the data here
        filename = "D:/Private/Python/Sources/data/bloom_filter.bin"

        with open(filename, "rb") as file:
            loaded_bloom_filter = pickle.load(file)

        return "Search data: "