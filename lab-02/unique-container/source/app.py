from cli import CLI
from container_controller import ContainerController

class App:
    _commands_info = '''
            add <key> [key, …] – add one or more elements to the container;
            remove <key> – delete key from container;
            find <key> [key, …] – check if the elements are presented in the container;
            list – print all elements of container;
            grep <regex> – check the value in the container by regular expression;
            save – save container to file;
            load – load container from file;
            switch – switches to another user;
            help - print commands information
    '''

    def print_commands_info(self, _):
        print(self._commands_info)

    def start_app(self):
        print(f'''Welcome to custom storage. Possible commands: {self._commands_info}''')
        
        controller = ContainerController()
        cli = CLI()

        commands = ['add', 'remove', 'find', 'list', 'grep', 'save', 'switch']
        for command in commands:
            cli.add_command(command, getattr(controller, command))

        cli.add_command('help', self.print_commands_info)

        while True:
            cli.parse_command()