class CLI:
    _commands: dict[str, callable]

    def __init__(self):
        self._commands = {}

    def add_command(self, command: str, function: callable):
        self._commands[command] = function
    
    def parse_command(self):
        command_with_args = input('Enter command: ').split(maxsplit=1)

        if not command_with_args:
            print('Empty command')
            return
        
        command = command_with_args[0]
        args = command_with_args[1] if len(command_with_args > 1) else ''

        function = self._commands.get(command)

        if function is None:
            print(f'Undefind command "{command}"')
            return
        
        function(args)