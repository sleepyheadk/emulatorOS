from src.app import App
from src.shell import Shell

TITLE = "MyVFS"
PROMPT = "~$ "

shell = Shell()
app = App(shell, TITLE, PROMPT)

app.mainloop()