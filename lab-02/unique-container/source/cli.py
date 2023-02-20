from container import UniqueContainer
import os

GREETING_MSG = '''
commands \n
add <key> [key, …] – add one or more elements to the container (if the element is already in there then don’t add);\n
remove <key> – delete key from container;\n
find <key> [key, …] – check if the element is presented in the container, print each found or “No such elements” if nothing is;\n
list – print all elements of container;\n
grep <regex> – check the value in the container by regular expression, print each found or “No such elements” if nothing is;\n
save/load – save container to file/load container from file;\n
switch – switches to another user.\n
'''

class CliModule:
    
    def run(self):
        self._container = UniqueContainer()
        os.system('clear')
        print(GREETING_MSG)
        login = input('Enter your login: ')
        self._container.login(login)
        operation = ''
        while operation != ':q':
            command = input('Enter command (:q to exit)\n').split(' ')
            operation = command[0]
            if operation == 'add':
                if len(command) == 1:
                    print('Please enter key when want to use add command')
                else:
                    self._container.add(command[1:])
            elif operation == 'remove':
                if len(command) == 1:
                    print('Please enter key when want to use remove command')
                else:
                    self._container.add(command[1:])
            elif operation == 'find':
                if len(command) == 1:
                    print('Please enter key when want to use find command')
                else:
                    self._container.add(command[1:])
            elif operation == 'list':
                if len(command) != 1:
                    print('list doesn\'t take any arguments')
                else:
                    self._container.list()
            elif operation == 'save':
                if len(command) != 1:
                    print('save doesn\'t take any arguments')
                else:
                    self._container.save()
            elif operation == 'switch':
                if len(command) != 2:
                    print('switch command requires one argument')
                else:
                    self._container.switch(command[1])
            elif operation == 'load':
                if len(command) != 2:
                    print('load command requires one argument')
                else:
                    self._container.load(command[1])
            elif operation == 'grep':
                if len(command) != 2:
                    print('grep command requires one argument')
                else:
                    self._container.grep(command[1])
            

