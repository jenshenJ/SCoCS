import pickle

class DbService():
    def save(self, container: set[str], container_filename: str):
        with open(container_filename, 'wb') as file:
            pickle.dump(container, file)


    def load(self, container_filename) -> set[str]:
        with open(container_filename, 'rb') as file:
            loaded_data = pickle.load(file)
            return loaded_data