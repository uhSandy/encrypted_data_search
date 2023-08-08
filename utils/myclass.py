from utils.searchclass import SearchClass
class MyClass:
    def __init__(self):
        pass

    def process_data(self, data):
        # Add your code to process the data here

        # Create an instance of the MyClass
        search_class_instance = SearchClass()

        # Call the method from the MyClass to process the data
        processed_data = search_class_instance.search_data("xxx")

        print(processed_data)
        print("---->>>>------")

        return "Processed data: " + data