import re
from container_service import ContainerService

class ContainerController:
    _container_service: ContainerService = None

    def __init__(self):
        self.switch()
  
    @staticmethod
    def _split_and_apply(keys: str, function: callable):
        for key in keys.split():
            function(key)

    def add(self, args: str):
        if not args:
            print('There is no any key to add provided')
            return
        
        self._split_and_apply(args, self._container_service.add)
        print('Keys added to container')

    def _remove_key(self, key: str):
        if self._container_service.find(key):
            self._container_service.remove(key)
        else:
            print(f'Key {key} not found')

    def remove(self, args: str):
        if not args:
            print('There is no any key to remove provided')
            return
        
        self._split_and_apply(args, self._container_service.remove)
    
    def find(self, args: str):
        if not args:
            print('There is no any key to find provided')
        else:
            self._split_and_apply(args, 
                                  lambda key: print(f'Key {key} is {"" if self._container_service.find(key) else " not"} exist')
                                  )

    def list(self, _):
        keys = self._container_service.list()
        if not keys:
            print('Container is empty')
        else:
            print(' '.join(keys))

    def grep(self, args: str):
        if not args:
            print('Empty regex')
            return
        
        try:
            regex = re.compile(args)
        except re.error:
            print('Cannot parse regex "{args}"')
            return
        
        result = self._container_service.grep(regex)
        if not result:
            print('No any key matches the regex')
            return
        
        print(' '.join(result))
    
    def load(self, _):
        self._container_service.load()
        print('Loaded succesfully')

    def save(self, _):
        self._container_service.save()
        print('Saved succesfully')

    def _ask_for_save(self):
        option = input('Do you want to save container?(y/n): ')

        if option.lower() in ['y', 'yes']:
            self._container_service.save()
    
    def _ask_for_load(self):
        if self._container_service.is_exists():
            option = input('Container was found. Do you want to load it?(y/n): ')

            if option.lower() in ['y', 'yes']:
                self._container_service.load()

    def switch(self, args=None):
        if self._container_service:
            self._ask_for_save()
        
        username = input('Enter new username: ')
        self._container_service = ContainerService(username)

        self._ask_for_load()
