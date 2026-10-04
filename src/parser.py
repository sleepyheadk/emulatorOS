def parse(line):
    '''
    Парсер, обрабатывающий введенную пользователем строку (комманду с аргументами).
    Реализована корректная обработка аргументов в кавычках.

    :param line: строка, введенная пользователем
    :return: список tokens с названием команды (первый элемент) и аргументами
    '''
    tokens = []
    current_argument = ""
    quote = None

    for char in line:
        if char == '"' or char == "'":
            if quote is None:
                quote = char
            elif quote == char:
                quote = None
            else:
                current_argument += char

        elif char == " ":
            if quote is not None:
                current_argument += char
            elif current_argument:
                tokens.append(current_argument)
                current_argument = ""

        else:
            current_argument += char

    if quote is not None:
        raise ValueError("unclosed quote")

    if current_argument:
        tokens.append(current_argument)

    return tokens