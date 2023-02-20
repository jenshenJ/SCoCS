from os import listdir
from os.path import isfile, join

DATA_PATH = '../data/'

class UniqueContainer:
    def __init__(self):
        self.data = set()
        self.user_list = [f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
        pass

    
    def login(self, username):
        self.username = username
        try:
            self.file = open(join('..', 'data', self.username), 'r+')
            self.data = set(self.file.read().split('||'))
        except FileNotFoundError:
            self.file = open(join('..', 'data', self.username), 'w+')     
    
    def save(self):
        self.file.close()
        file_path = join('..', 'data', self.username)
        self.file = open(file_path, 'w')
        data_str = '||'.join(list(self.data))
        self.file.write(data_str)


    def switch(self, new_login):
        if self.data != set(self.file.read().split('||')):
            print('You have unsaved changes. Do you want to save them? (Y/N)')
            option = ''
            options = ['y', 'Y', 'N', 'n']
            while option not in options:
                option = input()
            
            if option == 'y' or option == 'Y':
                self.save()
            
            self.login(new_login)
    