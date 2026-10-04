import tkinter as tk
import src.shell
from src.commands import EXIT

class App(tk.Tk):
    '''
    Класс App. Отвечает за управление графическим пользовательским интерфейсом.
    Наследуется от класса Tk.
    Объект класса - графическое окно.
    '''
    def __init__(self, shell, vfs_name, prompt):
        super().__init__()
        self.shell = shell
        self.title(f"VFS - {vfs_name}")
        self.geometry("640x240")

        self.output = tk.Text(self, wrap="word")
        self.output.pack(fill="both", expand=True)

        self.prompt = prompt

        self.output.bind("<Return>", self.on_return)
        self.output.bind("<Key>", self.on_key)
        self.output.bind("<ButtonRelease-1>", self.on_click_release)
        self.output.bind("<<Paste>>", self.on_paste)

        self.show_prompt()
        self.output.focus()

    def show_prompt(self):
        '''
        Показывает промпт на новой строке в виджете Text
        перед началом пользовательского ввода.
        '''
        self.output.insert("end", self.prompt)
        self.output.mark_set("input_start", "end-1c")
        self.output.mark_gravity("input_start", "left")
        self.output.mark_set("insert", "end-1c")
        self.output.see("end")

    def selection_touches_history(self):
        '''
        Проверяет, является ли выделенный пользователем текст
        историей (предыдущий ввод/вывод).

        :return True, если является, и False, если не является.
        '''
        if self.output.tag_ranges("sel"):
            return self.output.compare("sel.first", "<", "input_start")
        return False

    def move_cursor_to_end(self):
        '''
        Перемещает курсор в конец текста в виджете Text.

        Снимает текущее выделение и устанавливает позицию
        курсора после последнего символа текста.
        '''
        self.output.tag_remove("sel", "1.0", "end")
        self.output.mark_set("insert", "end-1c")

    def on_return(self, event):
        '''
        Обрабатывает нажатие клавиши Enter.

        Получает введённую пользователем команду, передаёт её
        в shell для выполнения и выводит результат в виджет Text.
        Если команда завершает работу программы, уничтожает окно.

        :param event: Событие нажатия клавиши Enter.
        :return: "break" для предотвращения стандартной обработки Enter.
        '''
        line = self.output.get("input_start", "end-1c")
        self.output.insert("end", '\n')

        result = self.shell.run_command(line)

        if result is EXIT:
            self.destroy()
            return "break"

        if result:
            self.output.insert("end", result + "\n")

        self.show_prompt()
        return "break"

    def on_key(self, event):
        '''
        Обрабатывает нажатия клавиш в виджете Text.

        Запрещает перемещение курсора и изменение текста в области
        истории команд, а также блокирует некоторые клавиши навигации.
        Разрешает редактирование только текущей строки ввода.

        :param event: Событие нажатия клавиши.
        :return: "break" для блокировки стандартной обработки события
             или None для продолжения стандартной обработки.
        '''
        key = event.keysym

        if key in ("Up", "Down", "Prior", "Next"):
            return "break"

        if key == "Home":
            self.output.mark_set("insert", "input_start")
            return "break"

        if key == "Left":
            if self.output.compare("insert", "<=", "input_start"):
                return "break"
            return None

        if key == "BackSpace":
            if self.output.compare("insert", "<=", "input_start") or self.selection_touches_history():
                return "break"
            return None

        if key == "Delete":
            if self.output.compare("insert", "<", "input_start") or self.selection_touches_history():
                return "break"
            return None

        if event.char and event.char.isprintable():
            if self.output.compare("insert", "<", "input_start") or self.selection_touches_history():
                self.move_cursor_to_end()
        return None

    def on_click_release(self, event):
        '''
        Обрабатывает отпускание кнопки мыши в виджете Text.

        Если курсор оказался в области истории команд и текст
        не выделен, перемещает курсор в конец текущего ввода.

        :param event: Событие отпускания кнопки мыши.
        '''
        if not self.output.tag_ranges("sel") and self.output.compare("insert", "<", "input_start"):
            self.output.mark_set("insert", "end-1c")

    def on_paste(self, event):
        '''
        Обрабатывает вставку текста в виджет Text.

        Если курсор находится в истории команд или выделение
        затрагивает историю, перемещает курсор в конец текущего ввода.

        :param event: Событие вставки текста.
        :return: None для продолжения стандартной обработки вставки.
        '''
        if self.output.compare("insert", "<", "input_start") or self.selection_touches_history():
            self.move_cursor_to_end()
        return None