EXIT = object()

def ls(args):
    '''
    Команда-заглушка ls

    :param args: список аргументов функции
    :return: строка, содержащая название и список аргументов функции
    '''
    return f"ls, args: {args}"

def cd(args):
    '''
    Команда-заглушка cd

    :param args: список аргументов функции
    :return: строка, содержащая название и список аргументов функции
    '''
    return f"cd, args: {args}"

def exit_cmd(args):
    '''
    Команда выхода.

    :param args: пустой, нужен для единообразия функций в run_command
    :return: объект EXIT или строку об ошибке, если есть аргументы.

    '''
    if args:
        return "exit: too many arguments"
    return EXIT

COMMANDS = {
    "ls": ls,
    "cd": cd,
    "exit": exit_cmd,
}