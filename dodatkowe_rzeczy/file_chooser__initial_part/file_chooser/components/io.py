class FileReader:

    def __init__(self, path_to_file):
        self.__path_to_file = path_to_file

    def read(self):
        with open(self.__path_to_file, "r") as f:
            for line in f:
                print(line)
