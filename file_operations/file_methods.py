import pickle

class File_Operation:
    def __init__(self):
        self.model_directory = 'model/'

    def load_model(self, filename):
        try:
            with open(self.model_directory + filename + '.P','rb') as f:
                return pickle.load(f)
        except Exception as e:
            raise Exception()
