from src.shell import Shell
from src.commands import EXIT

def test_run_simple_command():
    shell = Shell()
    result = shell.run_command("ls")
    assert result == "ls, args: []"

def test_run_command_with_argument():
    shell = Shell()
    result = shell.run_command("ls file.txt")
    assert result == "ls, args: ['file.txt']"

def test_run_command_with_multiple_arguments():
    shell = Shell()
    result = shell.run_command("cd folder test")
    assert result == "cd, args: ['folder', 'test']"

def test_run_command_with_quoted_argument():
    shell = Shell()
    result = shell.run_command('ls "my file.txt"')
    assert result == "ls, args: ['my file.txt']"

def test_empty_command():
    shell = Shell()
    result = shell.run_command("")
    assert result is None

def test_unknown_command():
    shell = Shell()
    result = shell.run_command("hello")
    assert result == "hello: command not found"

def test_unclosed_quote():
    shell = Shell()
    result = shell.run_command('ls "file.txt')
    assert result == "error: unclosed quote"

def test_exit_without_arguments():
    shell = Shell()
    result = shell.run_command("exit")
    assert result is EXIT

def test_exit_with_argument():
    shell = Shell()
    result = shell.run_command("exit 123")
    assert result == "exit: too many arguments"

def test_exit_with_multiple_arguments():
    shell = Shell()
    result = shell.run_command("exit one two")
    assert result == "exit: too many arguments"
