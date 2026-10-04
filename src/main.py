import argparse
import  os

from src.app import App
from src.shell import Shell

TITLE = "MyVFS"
PROMPT = "~$ "

def parse_args():
    '''
    Разбирает параметры командной строки с помощью argparse.

    Поддерживаемые параметры:
    --vfs - путь к физическому расположению VFS;
    --script - путь к стартовому скрипту.

    :return: объект Namespace с атрибутами vfs и script
             (None, если параметр не задан).
    '''
    parser = argparse.ArgumentParser(description="Эмулятор оболочки с VFS")
    parser.add_argument("--vfs", default=None,
                        help="путь к физическому расположению VFS")
    parser.add_argument("--script", default=None,
                        help="путь к стартовому скрипту")
    return parser.parse_args()

def read_script(path):
    '''
    Читает стартовый скрипт из файла.

    :param path: путь к файлу скрипта.
    :return: кортеж (список строк скрипта без символов переноса,
             сообщение об ошибке или None). При ошибке чтения
             список строк пустой.
    '''
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().splitlines(), None
    except OSError as e:
        return [], f"cannot read script '{path}': {e.strerror}"


def main():
    '''
    Точка входа в программу.

    Разбирает параметры командной строки, формирует и выводит
    отладочную информацию о них (в консоль и в окно), проверяет
    наличие VFS и читает стартовый скрипт. Затем создаёт Shell и App
    и запускает главный цикл окна.
    '''
    args = parse_args()

    debug = [
        "[DEBUG] Параметры запуска:",
        f"[DEBUG]   --vfs    = {args.vfs}",
        f"[DEBUG]   --script = {args.script}",
    ]

    if args.vfs is not None and not os.path.isdir(args.vfs):
        debug.append(f"[DEBUG] ОШИБКА: VFS '{args.vfs}' не найдена или не является папкой")

    script_lines = []
    if args.script is not None:
        script_lines, error = read_script(args.script)
        if error:
            debug.append(f"[DEBUG] ОШИБКА: {error}")

    for line in debug:
        print(line)

    shell = Shell(args.vfs)
    app = App(shell, TITLE, PROMPT,
              debug_info="\n".join(debug) + "\n",
              script_lines=script_lines)
    app.mainloop()


if __name__ == "__main__":
    main()