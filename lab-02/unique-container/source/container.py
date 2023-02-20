from os import listdir
from os.path import isfile, join

DATA_PATH = '../data/'

class UniqueContainer:
    def __init__(self):
        self.data = set()
        self.user_list = [f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
        pass

    
    def login(self, username: str):
        self.username = username
        try:
            self.file = open(join('..', 'data', self.username), 'r+')
            self.data = set(self.file.read().split('||'))
        except FileNotFoundError:
            self.file = open(join('..', 'data', self.username), 'w+') 
            self.user_list.append(self.username)    
    
    def save(self):
         if len(self.data & set(self.file.read().split('||'))) != len(self.data):
            print('You have unsaved changes. Do you want to save them? (Y/N)')
            option = ''
            options = ['y', 'Y', 'N', 'n']
            while option not in options:
                option = input()
            
            if option == 'y' or option == 'Y':
                self.file.close()
                file_path = join('..', 'data', self.username)
                self.file = open(file_path, 'w')
                data_str = '||'.join(list(self.data))
                self.file.write(data_str)

        
    def load(self, filename: str):
        file_path = join('..', 'data', self.username)
        if isfile(file_path):
            self.save()
            self.login(filename)
            print('Container', self.username, 'has been succesfully loaded')
        else:
            print("No such container")

        

    def switch(self, new_login: str):
        self.save()
        self.login(new_login)

    def add(self, elems: list):
        for elem in elems:
            self.data.add(elem)

    def remove(self, elem: str):
        if elem in self.data:
            self.data.remove(elem)
            print('Element is sucsessfully delete')
        else:
            print('There is no element', elem, 'in container')

    def find(self, elems: list):
        for elem in elems:
            if elem in self.data:
                print('Element ', elem, 'exists in container')
            else:
                print('Element', elem, 'hasn\'t found')
