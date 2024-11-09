utils.utils from Utils

class Transaction():
    def __init__(self, type, value, description = None):
        self.__type
        self.__value
        self.__description = description

        self.utils = utils()

    def save(self):
        self.__utils.write_file(self.__type, self.__value)

    def view(self):
        for line in self.__utils.read_file():
            print(line)