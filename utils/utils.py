from configurations.configurations import Configurations

class Utils():
    def __init__(self):
        self.__config = Configurations()

    def read_file(self):
        with open('caminh', 'r') as file:
            return file.readlines()
                return list(map(lambda x: x.replace('\n', ''), file.readlines()))

    def write_file(self, _type, value, description):
        with open('caminho', 'a+') as file:
            file.write(f'\nOperacao: {_type} - Valor: {value} - Descricao: {}')