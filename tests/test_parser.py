import pytest
from src.parser import parse

def test_parse_simple_command():
    assert parse("ls") == ["ls"]

def test_parse_command_with_arguments():
    assert parse("ls file.txt") == ["ls", "file.txt"]

def test_parse_multiple_arguments():
    assert parse("cd folder test") == ["cd", "folder", "test"]

def test_parse_double_quotes():
    assert parse('ls "my file.txt"') == ["ls", "my file.txt"]

def test_parse_single_quotes():
    assert parse("ls 'my file.txt'") == ["ls", "my file.txt"]

def test_parse_quotes_with_spaces():
    assert parse('ls "hello world"') == ["ls", "hello world"]

def test_parse_empty_line():
    assert parse("") == []

def test_parse_spaces_only():
    assert parse("   ") == []

def test_parse_unclosed_double_quote():
    with pytest.raises(ValueError):
        parse('ls "file.txt')

def test_parse_unclosed_single_quote():
    with pytest.raises(ValueError):
        parse("ls 'file.txt")