from src.parser import parse
from src.commands import  COMMANDS

class Shell:
    '''
    Класс Shell.
    Отвечает за обработку комманд.
    '''
    def __init__(self, vfs_path=None):
        self.commands = COMMANDS
        self.vfs_path = vfs_path

    def run_command(self, line):
        '''
        Обрабатывает введённую строку с помощью функции parse.

        :param line: Строка, введённая пользователем.
        :return:
            Результат выполнения команды;
            сообщение об ошибке при некорректных аргументах;
            None, если команда отсутствует.
        '''
        try:
            tokens = parse(line)
        except ValueError as e:
            return f"error: {e}"

        if not tokens:
            return None

        name, args = tokens[0], tokens[1:]
        command = self.commands.get(name)
        if command is None:
            return f"{name}: command not found"
        return command(args)
