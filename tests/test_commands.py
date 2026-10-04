from src.commands import ls, cd, exit_cmd, EXIT

def test_ls_without_arguments():
    assert ls([]) == "ls, args: []"

def test_ls_with_arguments():
    assert ls(["file.txt"]) == "ls, args: ['file.txt']"

def test_cd_without_arguments():
    assert cd([]) == "cd, args: []"

def test_cd_with_arguments():
    assert cd(["folder"]) == "cd, args: ['folder']"

def test_exit_without_arguments():
    assert exit_cmd([]) is EXIT

def test_exit_with_arguments():
    assert exit_cmd(["123"]) == "exit: too many arguments"

def test_exit_with_multiple_arguments():
    assert exit_cmd(["one", "two"]) == "exit: too many arguments"
