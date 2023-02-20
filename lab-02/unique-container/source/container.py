from os import listdir, path
from os.path import isfile, join
import os

DATA_PATH = '../data/'

class UniqueContainer:
    def __init__(self):
        self._data = set()
        
        if not path.exists('../data'):
            os.mkdir('../data')

        self._user_list = [f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
        pass

    
    def login(self, username: str):
        self._username = username
        try:
            self._file = open(join('..', 'data', self._username), 'r+')
            self._data = set(self._file.read().split('||'))
        except FileNotFoundError:
            self._file = open(join('..', 'data', self._username), 'w+') 
            self._user_list.append(self._username)    
    
    def save(self):
         if len(self._data & set(self._file.read().split('||'))) != len(self._data):
            print('You have unsaved changes. Do you want to save them? (Y/N)')
            option = ''
            options = ['y', 'Y', 'N', 'n']
            while option not in options:
                option = input()
            
            if option == 'y' or option == 'Y':
                self._file.close()
                file_path = join('..', 'data', self._username)
                self._file = open(file_path, 'w')
                data_str = '||'.join(list(self._data))
                self._file.write(data_str)

        
    def load(self, filename: str):
        file_path = join('..', 'data', filename)
        if isfile(file_path):
            new_file = open(join('..', 'data', filename), 'r+')
            new_data = set(new_file.read().split('||'))
            self._data |= new_data
            print('Container', filename, 'has been succesfully loaded')
        else:
            print("No such container")
    
    def switch(self, new_login: str):
        self.save()
        self.login(new_login)

    def add(self, elems: list):
        for elem in elems:
            self._data.add(elem)

    def remove(self, elem: str):
        if elem in self._data:
            self._data.remove(elem)
            print('Element is sucsessfully delete')
        else:
            print('There is no element', elem, 'in container')

    def find(self, elems: list):
        for elem in elems:
            if elem in self._data:
                print('Element ', elem, 'exists in container')
            else:
                print('Element', elem, 'hasn\'t found')

    def list(self):
        print('Elements of container:')
        for elem in self._data:
            print(elem)
